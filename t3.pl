
parent(tom, bob).
parent(bob, alice).
parent(bob, john).
parent(alice, mary).

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
male(tom).
male(bob).
male(john).

female(alice).
female(mary).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
grandfather(X, Y) :- male(X), grandparent(X, Y).
grandmother(X, Y) :- female(X), grandparent(X, Y).
