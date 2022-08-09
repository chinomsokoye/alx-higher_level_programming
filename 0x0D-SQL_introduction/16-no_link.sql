-- SQL script
-- lists all records of the second_table of the database in MySQL server
-- except rows without a name value

SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
