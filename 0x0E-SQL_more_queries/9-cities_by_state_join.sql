-- SQL script
-- lists all cities contained in the hbtn_0d_usa database

SELECT city.id, city.name, state.name FROM cities city
JOIN states state
WHERE city.state_id = state.id
ORDER BY city.id ASC;
