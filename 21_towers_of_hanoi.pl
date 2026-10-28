% Program 21: Towers of Hanoi
hanoi(1, Source, _, Destination) :-
    format('Move disk from ~w to ~w~n', [Source, Destination]).
hanoi(N, Source, Auxiliary, Destination) :-
    N > 1, N1 is N - 1,
    hanoi(N1, Source, Destination, Auxiliary),
    hanoi(1, Source, Auxiliary, Destination),
    hanoi(N1, Auxiliary, Source, Destination).

% Query: ?- hanoi(3, left, middle, right).
