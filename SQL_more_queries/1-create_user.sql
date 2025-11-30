-- 1-create_user.sql

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases and tables WITHOUT GRANT OPTION
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

