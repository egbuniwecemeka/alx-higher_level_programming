-- An SQL script that creates a DB hbtn_0d_2 and USER user_0d_2
-- User should have only SELECT privilege
-- USER pasword should be user_0d_2_pwd
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`
CREATE USER IF NOT EXISTS `user_0d_2` IDENTIFIED BY 'user_0d_2_pwd'
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';
