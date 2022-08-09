-- SQL script
-- displays max temperature of each state ordered by State name

SELECT state, MAX(value) AS max_temp FROM temperatures
ORDER BY state ASC;
