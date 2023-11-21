-- Create a table: force_name. in database hbtn_0d_2. Should not fail.
-- Column 1: id INT
-- Column 2: name VARCHAR(256) can’t be null
CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL
);
