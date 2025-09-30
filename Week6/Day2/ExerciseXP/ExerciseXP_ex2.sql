--In the dvdrental database write a query to select all the columns from the “customer” table.
SELECT * FROM customer;

--Write a query to display the names (first_name, last_name) using an alias named “full_name”.
SELECT first_name || ' ' || last_name as full_name
FROM customer;

--Write a query to select all the create_date from the “customer” table (there should be no duplicates).
SELECT DISTINCT create_date
FROM customer;

--Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.

SELECT * FROM customer ORDER BY first_name DESC;

--Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
SELECT * FROM film;

SELECT film_id,title, description,release_year,rental_rate FROM film ORDER BY rental_rate ASC;

--Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.

SELECT * FROM address;
SELECT address, phone FROM address where district = 'Texas';

--Write a query to retrieve all movie details where the movie id is either 15 or 150.
SELECT * FROM film WHERE film_id = '15' OR film_id = '150';

--Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.

SELECT film_id, title, description, length,rental_rate 
FROM film
WHERE title = 'Titanic';

-- Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
SELECT film_id, title,description,length,rental_rate FROM film WHERE title ILIKE 'ti%';

--Write a query which will find the 10 cheapest movies.
SELECT title,rental_rate FROM film ORDER BY rental_rate ASC,title ASC LIMIT 10;

--Write a query which will find the next 10 cheapest movies.
SELECT title,rental_rate FROM film ORDER BY rental_rate ASC,title ASC OFFSET 10 ROWS FETCH 	NEXT 10 ROWS ONLY;

--Write a query which will join the data in the customer table and the payment table.
--You want to get the first name and last name from the curstomer table, as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
SELECT * FROM customer;
SELECT * FROM payment;
SELECT c.first_name, c.last_name, p.amount,p.payment_date
FROM customer c
INNER JOIN payment p
ON c.customer_id = p.customer_id
ORDER BY c.customer_id ASC,p.payment_date ASC;

--Write a query to get all the movies which are not in inventory.
SELECT * FROM inventory;
SELECT * FROM film;
SELECT f.film_id,f.title, f.description,f.length,f.rental_rate
FROM film f
LEFT JOIN inventory i
	ON f.film_id = i.film_id
WHERE i.film_id is NULL;

--Write a query to find which city is in which country.

SELECT * FROM city;
SELECT * FROM country;
SELECT city.city, country.country
FROM city
INNER JOIN country
ON city.country_id = country.country_id;

-- You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.

SELECT * FROM staff;
SELECT * FROM customer;
SELECT * FROM payment;
SELECT c.customer_id,c.first_name, c.last_name,p.amount, p.payment_date,p.staff_id
FROM customer c
INNER JOIN payment p
ON c.customer_id = p.customer_id
ORDER BY p.staff_id ASC, c.customer_id ASC;


