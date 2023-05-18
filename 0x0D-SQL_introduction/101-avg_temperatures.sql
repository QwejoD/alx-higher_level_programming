-- Displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- Temperature
SELECT city, AVG(value) AS avg_temp FROM `temperatures` GROUP BY `city` ORDER BY AVG(value) desc;
