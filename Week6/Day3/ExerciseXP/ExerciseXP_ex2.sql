-- 1. Use UPDATE to change the language of some films. Make sure that you use valid languages.
SELECT * FROM film;
UPDATE film
SET language_id = 2
WHERE title = 'Airport Pollock';

SELECT title, language_id FROM film WHERE title = 'Airport Pollock';

--2. Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
SELECT * FROM customer;
SELECT * FROM store;
SELECT * FROM address;
-- The customer table has 2 foreign keys (store_id, address_id).
-- Because of these FK when inserting a new customer we must ensure that both the referenced store and adress records already exist.
-- We fist insert address (to get its address_id) and then insert teh customer record using addres_id and valid store_id.

--3.We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
-- Not an easy step because it is linked to new_film and language tables through FKs (film_id and language_id).
DROP TABLE customer_review;

--4.Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT * FROM rental;
SELECT COUNT(*)
FROM rental WHERE return_date IS NULL;
-- There are 183 outstanding rentals.

--5.Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT * FROM rental;
SELECT * FROM film;
SELECT * FROM inventory;

SELECT f.title,f.rental_rate
FROM rental r
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.rental_rate DESC
LIMIT 30;

--6.Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
--1) The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT * FROM film;
SELECT * FROM actor;
SELECT * FROM film_actor;

SELECT f.title,a.first_name,a.last_name,f.description
FROM actor a
JOIN film_actor fa ON fa.actor_id = a.actor_id
JOIN film f ON f.film_id = fa.film_id
WHERE 
a.first_name = 'Penelope'
AND a.last_name = 'Monroe'
AND f.description ILIKE '%sumo wrestler%';
--ANSWER: Park Citizen

--2)The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT * FROM film; --length,rating,film_id
SELECT * FROM category; -- category_id,name
SELECT * FROM film_category; --category_id,film_id

SELECT f.title,c.name,f.length,f.rating
FROM category c
JOIN film_category fc ON fc.category_id = c.category_id
JOIN film f ON f.film_id = fc.film_id
WHERE
c.name = 'Documentary'
AND f.length < 60
AND f.rating = 'R';
--ANSWER : Cupboard Sinners

--3) A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT * FROM customer; -- first_name,last_name,customer_id
SELECT * FROM film; -- rental_rate,film_id
SELECT * FROM rental; --customer_id, return_date
SELECT * FROM inventory; --inventory_id, film_id

SELECT f.title, f.rental_rate, cus.first_name,cus.last_name,r.return_date
FROM customer cus 
JOIN rental r ON r.customer_id = cus.customer_id
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
WHERE 
cus.first_name ='Matthew'
AND cus.last_name = 'Mahan'
AND f.rental_rate > 4
AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';
--ANSWER : Sugae Wonka

--4)The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
SELECT * FROM customer; -- first_name,last_name,customer_id
SELECT * FROM film; -- title,description,film_id,rental_rate
SELECT * FROM rental; --customer_id,inventory _id
SELECT * FROM inventory; --inventory_id, film_id

SELECT f.title,f.description,cus.first_name,cus.last_name,f.rental_rate
FROM customer cus 
JOIN rental r ON r.customer_id = cus.customer_id
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
WHERE 
cus.first_name ='Matthew'
AND cus.last_name = 'Mahan'
AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.rental_rate DESC 
LIMIT 1;
--ANSWER: Money Harold
