--CREATING A TABLE
-- CREATE TABLE actors(
-- actor_id SERIAL PRIMARY KEY,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(100) NOT NULL,
-- date_of_birth DATE NOT NULL,
-- number_oscars SMALLINT NOT NULL

-- )
--SEEING THE TABLE
-- SELECT * FROM actors

-- --ADD DATA INTO THE TABLE
-- INSERT INTO actors (first_name,last_name,date_of_birth,number_oscars)
-- VALUES ('Matt', 'Damon', '08/10/1970', 5)

-- SELECT * FROM actors
-- SHOW dateStyle

-- INSERT INTO actors(first_name,last_name,date_of_birth,number_oscars)
-- VALUES ('Angelina','Jolie','04/06/1975', 2)
-- SELECT * FROM actors
-- -- SHOW dateStyle

-- INSERT INTO actors(first_name,last_name,date_of_birth,number_oscars)
-- VALUES
-- -- ('Anne','Hathaway','12/11/1982', 1),
-- -- ('Natalie','Portman','09/06/1981',1);

-- -- Semi-colon allows to run diffrent querries on the same time

-- SELECT * FROM actors


-- DIFFERENT WAYS TO RETRIEVE AND DISPLAY DATA USING "SELECT"

-- SELECT last_name FROM actors

-- SELECT first_name,last_name FROM actors

-- --ADDING CONDITIONS USING "WHERE"
-- SELECT * FROM actors WHERE first_name = 'Angelina' AND last_name = 'Jolie'

-- INSERT INTO actors(first_name,last_name,date_of_birth,number_oscars)
-- VALUES('Angelina','Pery','04/09/1970', 0);

-- SELECT * FROM actors
-- LIKE AND ILIKE = LIKE is case sensitive AND ILIKE is not

-- SELECT * FROM actors WHERE first_name ILIKE 'n%'

-- SELECT * FROM actors WHERE first_name = 'Angelina' LIMIT 1

--HOW TO UPDATE,DELETE,ALTER

-- SELECT * FROM actors

-- to update a row
-- UPDATE actors
-- SET date_of_birth = '06/07/1980' WHERE first_name = 'Anne'
-- RETURNING 
-- *

--to update a table

-- ALTER TABLE actors RENAME COLUMN number_oscars TO oscars;
-- SELECT * FROM actors

-- to delete a row

-- DELETE FROM actors WHERE actor_id= 4
-- RETURNING 

-- SELECT * FROM actors

ALTER TABLE actors ADD COLUMN is_alive BOOLEAN;
SELECT * FROM actors


