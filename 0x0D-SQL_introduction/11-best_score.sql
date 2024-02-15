-- An sql script that list all records with a scroe >= 10 in a table of a DB
-- score should be ordered in descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC
