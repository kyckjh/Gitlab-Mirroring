DROP TABLE users;

CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phoneNumber TEXT NOT NULL,
balance INTEGER NOT NULL
);

.mode csv
.import users.csv users

ALTER TABLE users DROP COLUMN last_name;
ALTER TABLE users RENAME COLUMN first_name TO name;
ALTER TABLE users ADD COLUMN gender;

SELECT name, age, balance
  FROM users
 ORDER BY age, balance DESC;

-- .mode csv
-- .import users.csv users

SELECT name, age, balance
  FROM users
 ORDER BY age AND balance DESC;

-- .header on
-- .mode column
pragma table_info('albums');

DROP TABLE contacts;

SELECT first_name FROM users;
SELECT * FROM users;
SELECT last_name, 
       first_name, 
       balance 
  FROM users 
 WHERE balance >= 500000;

SELECT rowid, first_name, age, balance
  FROM users 
 ORDER BY age, balance;

SELECT DISTINCT country, first_name FROM users;

SELECT DISTINCT country 
  FROM users 
 ORDER BY country;

SELECT first_name, age 
  FROM users 
 WHERE age BETWEEN 20 AND 36 
 ORDER BY age ASC;

SELECT first_name, age
  FROM users
 WHERE first_name = '진호';

SELECT first_name, age
  FROM users
 WHERE first_name LIKE '%재%';

SELECT DISTINCT country
  FROM users
 WHERE country LIKE '__남_';

SELECT first_name, age, country
  FROM users
 WHERE country IN ('충청북도', '충청남도');

SELECT *
  FROM users
 WHERE country LIKE ('충청%');

SELECT *
  FROM users
 WHERE country LIKE ('충청%')
    OR country LIKE ('경상%')
 LIMIT 10;

SELECT first_name, age, balance
  FROM users
 WHERE age >= 35
   AND balance >= 500000;