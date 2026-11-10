(* Run the commands of the theories in the files named by TRACE_FILES one by one, printing the position and
   elapsed time of each, with a timeout of TRACE_TIMEOUT seconds (default 180); a theory finished earlier in the
   list serves as parent of later ones. A failing proof step is reported and replaced by sorry; failing that,
   the goal is re-run and closed by sorry, and the commands up to the next one that succeeds skipped. With
   TRACE_STOP set to a line number, stop before the command at that line and instead try each candidate proof
   text in the file TRACE_CANDIDATES (separated by lines of four dashes) from that state *)
let
  val files = space_explode " " (getenv "TRACE_FILES");
  val stop = (case getenv "TRACE_STOP" of "" => NONE | s => SOME (Value.parse_int s));
  val timeout = Time.fromSeconds (case getenv "TRACE_TIMEOUT" of "" => 180 | s => Value.parse_int s);
  val goal_commands =
    ["lemma", "theorem", "corollary", "proposition", "schematic_goal", "interpretation", "sublocale",
     "global_interpretation", "termination", "function"];
  fun is_goal tr = member (op =) goal_commands (Toplevel.name_of tr);
  fun where_ tr = Toplevel.name_of tr ^ " " ^ Position.here (Toplevel.pos_of tr);
  fun at_stop tr =
    (case (stop, Position.line_of (Toplevel.pos_of tr)) of (SOME l, SOME l') => l' >= l | _ => false);
  fun run tr st =
    let
      val start = Timing.start ();
      val st' = Timeout.apply timeout (Toplevel.command_exception true tr) st;
      val t = Timing.result start;
    in writeln (Timing.message t ^ " " ^ where_ tr); st' end;
  val error_text = Runtime.exn_message;
  fun candidates st =
    let
      val thy = Toplevel.theory_of st;
      fun group [] cur acc = rev (cat_lines (rev cur) :: acc)
        | group (l :: ls) cur acc =
            if l = "----" then group ls [] (cat_lines (rev cur) :: acc) else group ls (l :: cur) acc;
      val texts = group (split_lines (File.read (Path.explode (getenv "TRACE_CANDIDATES")))) [] [];
      fun try_one i text =
        let
          val trs = Outer_Syntax.parse_text thy (K thy) Position.none text;
          val start = Timing.start ();
          val outcome =
            (Timeout.apply timeout (fn () => fold (Toplevel.command_exception true) trs st) ();
             "OK")
            handle Timeout.TIMEOUT _ => "TIMEOUT" | exn => "FAIL\n" ^ error_text exn;
        in writeln ("CANDIDATE " ^ string_of_int i ^ ": " ^ outcome ^ "\n" ^ Timing.message (Timing.result start)) end;
    in fold_index (fn (i, text) => fn () => try_one (i + 1) text) texts () end;
  fun trace file done =
    let
      val master_dir = Path.dir (Path.explode file);
      val text = File.read (Path.explode file);
      val header = Thy_Header.read (Position.file file) text;
      fun parent name =
        (case AList.lookup (op =) done name of SOME thy => thy | NONE => Thy_Info.get_theory name);
      val parents = map (parent o fst) (#imports header);
      val thy0 = Resources.begin_theory master_dir header parents;
      val trs = Outer_Syntax.parse_text thy0 (K thy0) (Position.file file) text;
      val sorry = the_single (Outer_Syntax.parse_text thy0 (K thy0) Position.none "sorry");
      (* saved: goal command and state before it; skipping: after a recovery, until a command succeeds;
         stopped: the stop line reached *)
      fun step tr (st, saved, skipping, stopped) =
        if stopped orelse Toplevel.name_of tr = "<ignored>" then (st, saved, skipping, stopped)
        else if at_stop tr then (writeln ("STOP before " ^ where_ tr); (st, saved, skipping, true))
        else
        let
          val saved' = if is_goal tr then SOME (tr, st) else saved;
          val _ = if skipping then () else writeln ("START " ^ where_ tr);
        in
          (run tr st, saved', false, false) handle exn =>
            if skipping then (st, saved, true, false)
            else
              let
                val _ = writeln ("*** FAILED " ^ where_ tr ^ "\n" ^ error_text exn);
                val step_sorry =
                  if member (op =) ["by", ".", ".."] (Toplevel.name_of tr)
                  then SOME (Toplevel.command_exception true sorry st) handle _ => NONE
                  else NONE;
              in
                case step_sorry of SOME st' => (writeln ("*** STEP SORRIED " ^ where_ tr); (st', saved, false, false))
                | NONE =>
                (case saved of
                  SOME (goal, st0) =>
                    if Toplevel.pos_of goal = Toplevel.pos_of tr then raise exn
                    else
                      let val st' = Toplevel.command_exception true sorry (Toplevel.command_exception true goal st0)
                      in writeln ("*** SORRIED " ^ where_ goal); (st', NONE, true, false) end
                | NONE => raise exn)
              end
        end;
      val (st, _, _, stopped) = fold step trs (Toplevel.make_state NONE, NONE, false, false);
    in
      if stopped then (candidates st; (fst (#name header), thy0) :: done)
      else
        let val thy = Toplevel.end_theory Position.none st
        in writeln ("FINISHED " ^ file); (fst (#name header), thy) :: done end
    end;
in
  fold trace files []
end;
