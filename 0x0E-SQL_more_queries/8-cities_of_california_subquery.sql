-- SQL script
-- list all cities of California that can be found in the hbtn_0d_usa
-- result in ASC order

SELECT id, name FROM cities
WHERE state.id =
(SELECT id FROM states
WHERE name = 'California')
GROUP BY id ORDER BY id ASC;
