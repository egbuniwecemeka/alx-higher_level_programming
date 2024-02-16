-- SQL scripts that creates a user server user_0d_1
-- Grant all permission to user and set password to user_0d_1_pwd
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost
