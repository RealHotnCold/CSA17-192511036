% Program 24: Suggest a diet based on a condition.
% Educational example only; not medical advice.
diet_for(diabetes, whole_grains).
diet_for(diabetes, leafy_vegetables).
diet_for(hypertension, low_sodium_food).
diet_for(hypertension, fruits_and_vegetables).
diet_for(anemia, iron_rich_food).
diet_for(anemia, vitamin_c_rich_food).
diet_for(fever, fluids_and_soups).
diet_for(fever, easy_to_digest_food).

suggest_diet(Condition, Food) :-
    diet_for(Condition, Food).

% Queries:
% ?- suggest_diet(diabetes, Food).
% ?- suggest_diet(anemia, Food).
% ?- suggest_diet(fever, Food).
