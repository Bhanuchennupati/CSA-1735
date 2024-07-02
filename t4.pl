diet(flu, 'Stay hydrated with water, herbal tea, and clear broth. Consume foods rich in vitamin C like oranges, strawberries, and bell peppers.').
diet(diabetes, 'Focus on foods with a low glycemic index, such as whole grains, leafy greens, and lean proteins. Avoid sugary and processed foods.').
start :-
    write('Enter the disease for dietary recommendation (or type quit to exit):'), nl,
    read(Disease),
    handle_query(Disease).

handle_query(quit) :-
    write('Goodbye!'), nl.

handle_query(Disease) :-
    (diet(Disease, Recommendation) ->
        format('Diet recommendation for ~w: ~w~n', [Disease, Recommendation])
    ;
        format('No diet recommendation found for ~w.~n', [Disease])
    ),
    start.
