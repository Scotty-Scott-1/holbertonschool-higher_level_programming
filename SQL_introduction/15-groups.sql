-- list the number of each row with the same score. Display columns score and number(of scores) descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
