-- An SQL script that creates a DB hbtn_0d_2 and USER user_0d_2
-- CREATES a  DB if it dooes not exist
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
-- Creates a user if it does not exist with pasword access
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant SELECT privilege on the hbtn_0d_2 DB for user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
