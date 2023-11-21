-- Create a database: hbtn_0d_usa. Should not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use new database
USE hbtn_0d_usa;
-- Create a table: states. Should not fail.
-- Column 1: id INT unique, auto generated, can’t be null and is a primary key
-- Column 2: name VARCHAR(256) can’t be null
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	name VARCHAR(256) NOT NULL
);
