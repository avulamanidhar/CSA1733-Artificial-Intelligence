% Facts
fact(disease(diabetes)).
fact(disease(hypertension)).
fact(disease(obesity)).

fact(food(chicken_breast)).
fact(food(broccoli)).
fact(food(salmon)).

% Rules linking diseases to dietary recommendations
rule(eat_low_carb, [disease(diabetes)]).
rule(eat_low_sodium, [disease(hypertension)]).
rule(eat_low_calorie, [disease(obesity)]).

% Rules linking dietary recommendations to specific food items
rule(recommend(chicken_breast), [eat_low_carb]).
rule(recommend(broccoli), [eat_low_sodium]).
rule(recommend(salmon), [eat_low_calorie]).

% Backward chaining
backward_chain(Query) :-
    rule(Query, Body),
    loop(Body),
    write(Query),
    write(' is recommended.'),
    nl.

loop([]).
loop([Condition|Body]) :-
    fact(Condition),
    loop(Body),
    !.
loop([Condition|Body]) :-
    backward_chain(Condition),
    loop(Body),
    !.

% Display known facts and rules
display_facts :-
    fact(Fact),
    write(Fact),
    nl,
    fail.
display_facts.

display_rules :-
    rule(Head, Body),
    write('Rule: '),
    write(Head),
    write(' :- '),
    write(Body),
    nl,
    fail.
display_rules.

% Main predicate to display facts and rules
main :-
    write('Known Facts:'),
    nl,
    display_facts,
    write('Recommendations:'),
    nl,
    display_rules,
    !.

% Query to print full recommendation for a disease
full_recommendation(Disease) :-
    rule(DietRecommendation, [disease(Disease)]),
    rule(FoodRecommendation, [DietRecommendation]),
    write('For '), write(Disease), write(', it is recommended to '), write(DietRecommendation), nl,
    write('A good food option is '), write(FoodRecommendation), write('.'), nl.

% Run main
:- main.
