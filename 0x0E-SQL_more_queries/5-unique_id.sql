-- SQL script
-- creates table unique_id on MySQL
-- description id, name

CREATE TABLE IF NOT EXISTS unique_id (
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256)
);
