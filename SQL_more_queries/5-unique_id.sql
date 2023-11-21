-- Create a table: unique_id. Should not fail.
-- Column 1: id INT with the default value 1 and must be unique
-- Column 2: name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
