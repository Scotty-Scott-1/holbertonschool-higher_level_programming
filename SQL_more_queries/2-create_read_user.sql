-- Create a database: hbtn_0d_2. Should not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create a user: user_0d_2. Should not fail.
-- Set password to: user_0d_2_pwd
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- User should only have SELECT privilages
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
