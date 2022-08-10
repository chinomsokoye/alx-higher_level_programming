-- SQL script
-- list all cities of California that can be found in the hbtn_0d_usa
-- result in ASC order

SELECT city.id, city.name FROM cities city, states st
WHERE city.id = st.id
ORDER BY city.id ASC;
