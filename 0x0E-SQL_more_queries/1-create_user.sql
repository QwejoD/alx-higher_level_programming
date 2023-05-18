-- Creates the MySQL server user user_0d_1
-- user_0d_1 should have all privileges and password should be set to user_0d_1_pwd, Fails if user_0d_1 alreadyy exists
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
