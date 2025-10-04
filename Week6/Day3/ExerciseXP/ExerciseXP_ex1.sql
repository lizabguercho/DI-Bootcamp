--1.Get a list of all the languages, from the language table.
SELECT * FROM language ;
SELECT name FROM language;

--2.Get a list of all films joined with their languages – select the following details : film title, description, and language name.
SELECT * FROM film;

SELECT f.title,f.description,l.name
FROM film f
INNER JOIN language l
ON f.language_id = l.language_id;

--3. Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name
SELECT f.title,f.description,l.name as language_name
FROM language l
LEFT JOIN film f
ON f.language_id = l.language_id
ORDER BY l.name,f.title;

-- 4. Create a new table called new_film with the following columns : id, name. Add some new films to the table.
CREATE TABLE new_film(
film_id SERIAL,
film_name VARCHAR(45) NOT NULL,
PRIMARY KEY (film_id)
);
ALTER TABLE new_film
RENAME COLUMN film_name TO title;

SELECT * FROM new_film;

INSERT INTO new_film (film_name)
VALUES ('The Brutalist'),('A Real Pain');

--5. Create a new table called customer_review, which will contain film reviews that customers will make.

CREATE TABLE customer_review(
review_id SERIAL PRIMARY KEY NOT NULL,
film_id INT NOT NULL REFERENCES new_film(film_id) ON DELETE CASCADE,
language_id INT NOT NULL REFERENCES language(language_id),
title VARCHAR(100) NOT NULL,
score INT NOT NULL CHECK(score BETWEEN 1 AND 10),
text_review TEXT,
last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
SELECT * FROM customer_review;

--6.Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

INSERT INTO customer_review(film_id,language_id,title,score,text_review)
VALUES(
(SELECT nf.film_id FROM new_film nf WHERE nf.title = 'The Brutalist' LIMIT 1),
(SELECT l.language_id FROM language l WHERE l.name = 'English' LIMIT 1),
'The Brutalist', 10, ' Impressive story of a Jewish Architect and his career development throughout years. Bravo!')
RETURNING review_id;

INSERT INTO customer_review(film_id,language_id,title,score,text_review)
VALUES(
(SELECT nf.film_id FROM new_film nf WHERE nf.title = 'A Real Pain' LIMIT 1),
(SELECT l.language_id FROM language l WHERE l.name = 'English' LIMIT 1),
'A Real Pain', 9, 'Life changing trip of cousins to places where they grandmother used to live. A pure connection with ancestry in a charming and funny way.')
RETURNING review_id;

--7.Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film WHERE title = 'The Brutalist';
SELECT * FROM new_film;
SELECT * FROM customer_review;

