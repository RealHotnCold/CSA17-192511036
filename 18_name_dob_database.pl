% Program 18: Database with name and date of birth.
% Facts: person(Name, DateOfBirth).
person(alice, date(15, 3, 2004)).
person(bob, date(22, 7, 2003)).
person(charlie, date(9, 11, 2004)).
person(david, date(1, 1, 2005)).

% Queries:
% ?- person(Name, DOB).
% ?- person(bob, DOB).
% ?- person(Name, date(_, _, 2004)).
