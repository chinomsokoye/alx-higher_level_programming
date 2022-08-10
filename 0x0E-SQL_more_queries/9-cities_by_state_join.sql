-- SQL script
-- lists all cities contained in the hbtn_0d_usa database

SELECT city.id, city.name, st.name FROM cities city, states st
WHERE city.state_id = st.id
GROUP BY city.id ASC;
