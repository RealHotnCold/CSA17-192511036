% Program 25: Monkey and Banana problem
% State: state(MonkeyPosition, MonkeyHeight, BoxPosition, HasBanana)

move(state(P, on_floor, P, no), climb,
     state(P, on_box, P, no)).
move(state(middle, on_box, middle, no), grab_banana,
     state(middle, on_box, middle, yes)).
move(state(P1, on_floor, P1, no), push_box(P1, P2),
     state(P2, on_floor, P2, no)) :-
    P1 \= P2.
move(state(P, on_box, P, no), climb_down,
     state(P, on_floor, P, no)).

solve_monkey(State, []) :-
    State = state(_, _, _, yes).
solve_monkey(State, [Action | Rest]) :-
    move(State, Action, NextState),
    solve_monkey(NextState, Rest).

% Query:
% ?- solve_monkey(state(door, on_floor, window, no), Plan).
