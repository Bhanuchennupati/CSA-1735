initial_state(state(at_door, at_window, false, false)).
goal_state(state(_, _, _, true)).
action(grasp, state(middle, middle, true, false), state(middle, middle, true, true)).
action(climb, state(Pos, Pos, false, HasBananas), state(Pos, Pos, true, HasBananas)).
action(push_box(Pos1, Pos2), state(Pos1, Pos1, false, HasBananas), state(Pos2, Pos2, false, HasBananas)).
action(walk(Pos1, Pos2), state(Pos1, Box, false, HasBananas), state(Pos2, Box, false, HasBananas)).

position(at_door).
position(at_window).
position(middle).
plan(State, [], _) :- goal_state(State).
plan(State, [Action|Rest], Visited) :-
    action(Action, State, NewState),
    \+ member(NewState, Visited),
    plan(NewState, Rest, [NewState|Visited]).
find_plan :-
    initial_state(InitialState),
    plan(InitialState, Plan, [InitialState]),
    write('Plan to get the bananas: '), nl,
    write(Plan), nl.
