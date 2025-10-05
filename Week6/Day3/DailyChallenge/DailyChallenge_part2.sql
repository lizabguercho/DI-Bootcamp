--PART II

--Creating a TABLE book
CREATE TABLE book(
book_id SERIAL PRIMARY KEY,
title TEXT NOT NULL,
author VARCHAR(50) NOT NULL
);
-- Adding 3 books with their title and authors
INSERT INTO book(title,author)
VALUES 
('Alice in Wonderland','Lewis Carroll'),('Harry Potter','J.K Rowling'),('To kill a mockingbird','Harper Lee');

SELECT * FROM book;

--Creating table Student 

CREATE TABLE student(
student_id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL UNIQUE,
age INT CHECK(age<= 15) -- adding a constraint to have age below 15
);

-- Adding name and age of all students
INSERT INTO student(name,age)
VALUES 
('John', 12),('Lera', 11),('Patrick', 10),('Bob', 14);

SELECT * FROM student;

--Creating a library table which are linked to book and student tables (Many-to-many relationship)
CREATE TABLE library(
book_fk_id INT REFERENCES book(book_id)
ON DELETE CASCADE 
ON UPDATE CASCADE,
student_fk_id INT REFERENCES student(student_id)
ON DELETE CASCADE 
ON UPDATE CASCADE,
borrowed_date TIMESTAMP,
PRIMARY KEY (book_fk_id, student_fk_id)
);

SELECT * FROM library;

--Adding information about student,which book she/he rented and when
INSERT INTO library(book_fk_id, student_fk_id, borrowed_date)
VALUES
((SELECT book_id FROM book WHERE title = 'Alice in Wonderland'),
(SELECT student_id FROM student WHERE name = 'John'),'2022-02-15'),

((SELECT book_id FROM book WHERE title = 'To kill a mockingbird'),
(SELECT student_id FROM student WHERE name = 'Bob'),'2021-03-03'),

((SELECT book_id FROM book WHERE title = 'Alice in Wonderland'),
(SELECT student_id FROM student WHERE name = 'Lera'),'2021-05-25'),

((SELECT book_id FROM book WHERE title = 'Harry Potter'),
(SELECT student_id FROM student WHERE name = 'Bob'),'2021-08-12');


-- Select all the columns from the junction table
SELECT * FROM library;
-- Select the name of the student and the title of the borrowed books
SELECT s.name student_name, b.title book_title
FROM library l
JOIN student s ON l.student_fk_id = s.student_id
JOIN book b ON l.book_fk_id = b.book_id;

--Select the average age of the children, that borrowed the book Alice in Wonderland

SELECT ROUND(AVG(s.age),2) as average_age_of_readers
FROM library l
JOIN student s ON l.student_fk_id = s.student_id
JOIN book b ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice in Wonderland';

-- Delete a student from the Student table, what happened in the junction table ?

DELETE FROM student
WHERE student_id = 4;

--The student with student_id = 4 is deleted from the student table.
--Any rows in library with student_fk_id = 4 are also automatically removed.