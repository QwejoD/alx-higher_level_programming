-- Lists all records with a score >= 10 in the table second_table of the database 
-- Display the best score ordered in descending order
SELECT score, name FROM `second_table` WHERE `score` >= 10 ORDER BY `score` desc;
