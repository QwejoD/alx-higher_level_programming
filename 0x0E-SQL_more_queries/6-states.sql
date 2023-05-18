-- Creates the database hbtn_0d_usa and the table states
-- Creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switch to the database
USE hbtn_0d_usa;
-- Creating a table including the descriptions
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);
