-- List a rows of a second_table in database hbtn_0c_0. Display score and name. Highest score frist. Only scores >=10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
