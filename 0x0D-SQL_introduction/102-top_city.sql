-- SQL script
-- displays the top 3 of cities temperature during July and August ordered by
--- temperature in desc

SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month = 7 AND month = 8
ORDER BY avg_temp DESC LIMIT 3;
