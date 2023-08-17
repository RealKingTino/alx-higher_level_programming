-- Create or update the database hbtn_0d_2
CREATE DATABASE
	IF NOT EXISTS hbtn_0d_2;
-- Create or update user_0d_2 with the password user_0d_2_pwd
CREATE USER
	IF NOT EXISTS 'user_0d_2'@'localhost'
	IDENTIFIED BY 'user_0d_2_pwd';
-- Grant usage and SELECT privilege to user_0d_2 for the database hbtn_0d_2
GRANT USAGE
	ON *.*
	TO 'user_0d_2'@'localhost';
GRANT SELECT
	ON `hbtn_0d_2`.*
	TO 'user_0d_2'@'localhost';
