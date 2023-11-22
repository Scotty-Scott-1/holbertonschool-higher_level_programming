-- Create database: hbtn_0d_usa. Should not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use new database
USE hbtn_0d_usa;
-- Create table: cities. Should not fail.
-- Column 1: id INT unique, auto generated, can’t be null and is a primary key
-- Column 2: state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
-- Column 3: name VARCHAR(256) can’t be null
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id)
);
