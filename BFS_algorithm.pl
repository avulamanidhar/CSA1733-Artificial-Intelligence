:- dynamic frontier/1, explored/1.

% Define edges with weights
edge(a, b, 10).
edge(a, c, 1).
edge(b, d, 5).
edge(c, d, 2).
edge(c, e, 7).
edge(d, e, 6).

% Define heuristics
heuristic(a, 0).
heuristic(b, 3).
heuristic(c, 4).
heuristic(d, 2).
heuristic(e, 0).

% Best-First Search
best_first_search(Start, Goal, Path) :-
    retractall(frontier(_)),
    retractall(explored(_)),
    assert(frontier([[Start, [Start], 0]])),
    assert(explored([])),
    loop(Goal, Path).

loop(Goal, Path) :-
    frontier([[Node, PathSoFar, _]|RestFrontier]),
    retract(frontier(_)),
    assert(frontier(RestFrontier)),
    (   Node = Goal
    ->  reverse(PathSoFar, Path)
    ;   findall([Neighbor, [Neighbor|PathSoFar], NewCost],
                (   edge(Node, Neighbor, Cost),
                    heuristic(Neighbor, Heuristic),
                    NewCost is Cost + Heuristic,
                    \+ member(Neighbor, PathSoFar)
                ),
                Neighbors),
        sort(Neighbors, SortedNeighbors),
        retract(frontier(CurrentFrontier)),
        append(SortedNeighbors, CurrentFrontier, NewFrontier),
        assert(frontier(NewFrontier)),
        loop(Goal, Path)
    ).

% Helper predicates
reverse(L, R) :- reverse(L, [], R).
reverse([], R, R).
reverse([H|T], Acc, R) :- reverse(T, [H|Acc], R).

member(X, [X|_]).
member(X, [_|T]) :-
    member(X, T).

sort([], []).
sort([X], [X]).
sort([X,Y|T], Sorted) :-
    (   X =< Y
    ->  Sorted = [X|SortedT],
        sort([Y|T], SortedT)
    ;   Sorted = [Y|SortedT],
        sort([X|T], SortedT)
    ).
