-- Lists the cities in California
-- Use a subquery to get the correct state id from states
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id from states
	WHERE name = "California"
)
ORDER BY id ASC;
