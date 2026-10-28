% Program 23: Family tree
% parent(Parent, Child)
parent(john, mary).
parent(john, peter).
parent(mary, anna).
parent(mary, sam).
parent(peter, lisa).
parent(peter, david).

male(john).
male(peter).
male(sam).
male(david).
female(mary).
female(anna).
female(lisa).

father(Father, Child) :-
    parent(Father, Child), male(Father).
mother(Mother, Child) :-
    parent(Mother, Child), female(Mother).
grandparent(Grandparent, Child) :-
    parent(Grandparent, Parent), parent(Parent, Child).
sibling(Person1, Person2) :-
    parent(Parent, Person1), parent(Parent, Person2),
    Person1 \= Person2.

% Queries:
% ?- parent(john, Who).
% ?- grandparent(Who, anna).
% ?- sibling(mary, peter).
