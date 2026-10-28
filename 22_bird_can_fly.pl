% Program 22: Check whether a bird can fly
bird(sparrow).
bird(pigeon).
bird(eagle).
bird(ostrich).
bird(penguin).

flightless(ostrich).
flightless(penguin).

can_fly(Bird) :-
    bird(Bird),
    \+ flightless(Bird).

% Queries:
% ?- can_fly(sparrow).
% ?- can_fly(penguin).
% ?- can_fly(Bird).
