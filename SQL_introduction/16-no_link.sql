-- Display all rows of second_table. Don't select the column id. By score descensing. Check for null values and empty strings
SELECT score, name
FROM second_table
WHERE name != "" AND name IS NOT NULL
ORDER BY score DESC;
