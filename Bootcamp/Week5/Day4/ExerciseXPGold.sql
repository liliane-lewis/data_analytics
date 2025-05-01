-- Please create column(s) first...

-- Exercise 1: DVD Rental
--Instructions

--    You were hired to babysit your cousin and you want to find a few movies that he can watch with you.
--        Find out how many films there are for each rating.

SELECT rating, COUNT(*) AS total_films FROM film GROUP BY rating;
        
--Get a list of all the movies that have a rating of G or PG-13.

SELECT title, rating FROM film WHERE rating = 'G' OR rating = 'PG-13';
-- or SELECT title, rating FROM film WHERE rating IN ('G', 'PG-13');

-- Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.
SELECT title, rating, length, rental_rate FROM film WHERE rating IN ('G', 'PG-13') AND length < 120 AND rental_rate < 3.00 ORDER BY title ASC;


-- Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
UPDATE customer SET first_name = 'Liliane', last_name = 'Zukerman', email = 'liliane@any.com' WHERE customer_id = 1;

-- Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).

UPDATE address SET address = '1 Street St', address2 = 'Apt 13', district = 'Netanya', postal_code = '67890', phone = '051-1234567' WHERE address_id = 5x;

-- Exercise 2: students table
-- Instructions

-- Continuation of the Day1 Exercise XPGold : students table 


CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  last_name VARCHAR(50),
  first_name VARCHAR(50),
  birth_date DATE
);

INSERT INTO students (last_name, first_name, birth_date) VALUES
('Benichou', 'Marc', '1998-11-02'),
('Cohen', 'Yoan', '2010-12-03'),
('Benichou', 'Lea', '1987-07-27'),
('Dux', 'Amelia', '1996-04-07'),
('Grez', 'David', '2003-06-14'),
('Simpson', 'Omer', '1980-10-03'),
('Zukerman', 'Liliane', '1970-01-01');


-- Update
--
--    ‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates. Update both their birth_dates to 02/11/1998.
UPDATE students SET birth_date = '1998-11-02' WHERE (first_name = 'Lea' AND last_name = 'Benichou') OR (first_name = 'Marc' AND last_name = 'Benichou');

--    Change the last_name of David from ‘Grez’ to ‘Guez’.
 UPDATE students SET last_name = 'Guez' WHERE first_name = 'David' AND last_name = 'Grez';

--Delete
--
--   Delete the student named ‘Lea Benichou’ from the table.
DELETE FROM students WHERE first_name = 'Lea' AND last_name = 'Benichou';

--Count

--   Count how many students are in the table.
SELECT COUNT(*) FROM students;

--    Count how many students were born after 1/01/2000.
SELECT COUNT(*) FROM students WHERE birth_date > '2000-01-01';


--Insert / Alter

--    Add a column to the student table called math_grade.
ALTER TABLE students ADD COLUMN math_grade INTEGER;

--    Add 80 to the student which id is 1.
UPDATE students SET math_grade = 80 WHERE id = 1;


--    Add 90 to the students which have ids of 2 or 4.
UPDATE students SET math_grade = 90 WHERE id IN (2, 4);

--    Add 40 to the student which id is 6.
UPDATE students SET math_grade = 40 WHERE id = 6;

--    Count how many students have a grade bigger than 83
SELECT COUNT(*) FROM students WHERE math_grade > 83;

--    Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70.
INSERT INTO students (last_name, first_name, birth_date, math_grade) SELECT last_name, first_name, birth_date, 70 FROM students WHERE first_name = 'Omer' AND last_name = 'Simpson' LIMIT 1;

--    Now, in the table, ‘Omer Simpson’ should appear twice. It’s the same student, although he received 2 different grades because he retook the math exam.


--    Bonus: Count how many grades each student has.
--        Tip: You should display the first_name, last_name and the number of grades of each student. If you followed the instructions above correctly, all the students should have 1 math grade, except Omer Simpson which has 2.
--        Tip : Use an alias called total_grade to fetch the grades.
--        Hint : Use GROUP BY.
SELECT first_name, last_name, COUNT(math_grade) AS total_grade FROM students GROUP BY first_name, last_name

--SUM
--
--    Find the sum of all the students grades.

SELECT SUM(math_grade) AS total_sum FROM students;



---Exercise 3 : Items and customers
---Instructions

--We will work on the public database that we created yesterday.
CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  price INT
);

INSERT INTO items (id, name, price) VALUES
(1, 'Small Desk', 100),
(2, 'Large Desk', 300),
(3, 'Fan', 80);



CREATE TABLE customers (
  id SERIAL PRIMARY KEY,
  firstname VARCHAR(50),
  lastname VARCHAR(50)
);


INSERT INTO customers (firstname, lastname) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

--Part I

--    1. Create a table named purchases. It should have 3 columns :
--        1. id : the primary key of the table
--        2. customer_id : this column references the table customers
--        3. item_id : this column references the table items
--        4. quantity_purchased : this column is the quantity of items purchased by a certain customer
CREATE TABLE purchases (
  id SERIAL PRIMARY KEY,
  customer_id INT REFERENCES customers(id),
  item_id INT REFERENCES items(id),
  quantity_purchased INT
);



---    2. Insert purchases for the customers, use subqueries:
--        1. Scott Scott bought one fan
  INSERT INTO purchases (customer_id, item_id, quantity_purchased)
    VALUES (
        (SELECT id FROM customers WHERE firstname = 'Scott' AND lastname = 'Scott'),
        (SELECT id FROM items WHERE name = 'Fan'),
    1
    ); 
--        2. Melanie Johnson bought ten large desks
    INSERT INTO purchases (customer_id, item_id, quantity_purchased)
    VALUES (
        (SELECT id FROM customers WHERE firstname = 'Melanie' AND lastname = 'Johnson'),
        (SELECT id FROM items WHERE name = 'Large Desk'),
    10
    );
--        3. Greg Jones bougth two small desks

    INSERT INTO purchases (customer_id, item_id, quantity_purchased)
        VALUES (
            (SELECT id FROM customers WHERE firstname = 'Greg' AND lastname = 'Jones'),
            (SELECT id FROM items WHERE name = 'Small Desk'),
        2
    );

--    Here is the explanation of the first row:

--    id = 1, this is the auto-incrementing primary key
--    customer_id = 3, because the id of Scott Scott in the customers table is 3
--    item_id = 3, because the id of a fan in the items table is 3
--    quantity_purchased = 1, because Scott Scott bought one fan


--Part II

--    1. Use SQL to get the following from the database:
--        1. All purchases. Is this information useful to us?
SELECT * FROM purchases;

--        2. All purchases, joining with the customers table.
SELECT purchases.*, customers.firstname, customers.lastname
FROM purchases
JOIN customers ON purchases.customer_id = customers.id;

--        3. Purchases of the customer with the ID equal to 5.
SELECT * FROM purchases
WHERE customer_id = 5;


--        4. Purchases for a large desk AND a small desk
SELECT * FROM purchases WHERE item_id IN (SELECT id FROM items WHERE name IN ('Large Desk', 'Small Desk'));

--    2. Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
--        1. Customer first name
--        2. Customer last name
--        3. Item name
SELECT customers.firstname, customers.lastname, items.name AS item_name
    FROM purchases
        JOIN customers ON purchases.customer_id = customers.id
        JOIN items ON purchases.item_id = items.id;
    
--    3. Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work?  Why/why not?
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (1, NULL, 1);

-- It does not work. item_id must allow NULL values
