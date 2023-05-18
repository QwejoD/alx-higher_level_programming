-- lists the number of records with the same score in the table second_table of the database
-- Results display the score, with the label number
SELECT score , COUNT(score) AS number FROM `second_table` GROUP BY score ORDER BY score desc;
