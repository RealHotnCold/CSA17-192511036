% Program 20: Database of planets.
% Facts: planet(Name, OrderFromSun, Type).
planet(mercury, 1, terrestrial).
planet(venus, 2, terrestrial).
planet(earth, 3, terrestrial).
planet(mars, 4, terrestrial).
planet(jupiter, 5, gas_giant).
planet(saturn, 6, gas_giant).
planet(uranus, 7, ice_giant).
planet(neptune, 8, ice_giant).

% Queries:
% ?- planet(Name, Order, Type).
% ?- planet(Name, 3, Type).
% ?- planet(Name, _, gas_giant).
% ?- planet(earth, Order, Type).
