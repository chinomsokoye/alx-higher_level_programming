-- SQL script
-- lists number of records with same score in the table in MySQL server

SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score DESC;
