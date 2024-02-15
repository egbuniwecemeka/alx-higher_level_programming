-- An SQL script that lists the number of records with the same score in second_table of a DB of MySQL server
-- Order score according to descending order
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;

