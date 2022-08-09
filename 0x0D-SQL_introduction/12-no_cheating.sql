-- SQL script
-- updates the score of Bob to 10 in the table second_table

UPDATE second_table AS st
SET st.score = 10
WHERE st.name = "Bob";
