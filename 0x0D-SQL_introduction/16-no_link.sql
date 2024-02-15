-- An SQL scipt that list all records of second_table of a DB of MySQL server
-- Dont list rows without a name value
-- Order score in descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
