-- Create a table: id_not_null. Should not fail.
-- Column 1: id INT with the default value 1
-- Column 2: name VARCHAR(256)
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)
);
