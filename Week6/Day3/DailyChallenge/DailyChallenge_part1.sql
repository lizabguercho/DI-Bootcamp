--PART I
--Creating table customer
CREATE TABLE customer(
id SERIAL PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(100) NOT NULL
);
SELECT * FROM customer;

--Creating table customer_profile where customer_id is linked to customer table
CREATE TABLE customer_profile(
id SERIAL PRIMARY KEY,
isLoggedIn BOOLEAN DEFAULT false,
customer_id INT NOT NULL UNIQUE REFERENCES customer(id)
);

SELECT * FROM customer_profile;

-- Adding 3 customers to customer table
INSERT INTO customer(first_name,last_name)
VALUES 
('John','Doe'),('Jerome','Lalu'),('Lea','Rive');

-- Adding information whether person is logged in or NOT
INSERT INTO customer_profile(isLoggedIn,customer_id)
VALUES 
(true,(SELECT id FROM customer WHERE first_name = 'John')),
(false,(SELECT id FROM customer WHERE first_name = 'Jerome'));



--Show first_name of LoggedIn customers
SELECT c.first_name
FROM customer c
JOIN customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = true;

-- Show all the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
SELECT c.first_name,cp.isLoggedIn
FROM customer c 
LEFT JOIN customer_profile cp 
ON c.id = cp.customer_id;

--Show the number of customers that are not LoggedIn
SELECT COUNT(*) not_logged_in
FROM customer_profile
WHERE isLoggedIn = false;

