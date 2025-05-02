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


--Exercise 1 : Bonus Public Database (Continuation of XP)
--Instructions

--    Fetch the last 2 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
SELECT firstname, lastname FROM customers ORDER BY lastname ASC, firstname ASC LIMIT 2 OFFSET 3;

--    Use SQL to delete all purchases made by Scott.
DELETE FROM purchases WHERE customer_id = ( SELECT id FROM customers WHERE firstname = 'Scott' AND lastname = 'Scott'
);

 ---   Does Scott still exist in the customers table, even though he has been deleted? Try and find him.
 SELECT * FROM customers WHERE firstname = 'Scott' AND lastname = 'Scott';

--Use SQL to find all purchases. Join purchases with the customers table, so that Scott’s order will appear, although instead of the customer’s first and last name, you should only see empty/blank. (Which kind of join should you use?).
 SELECT
  p.id AS purchase_id,
  c.firstname,
  c.lastname,
  p.item_id,
  p.quantity_purchased
FROM purchases p
LEFT JOIN customers c ON p.customer_id = c.id;

--Use SQL to find all purchases. Join purchases with the customers table, so that Scott’s order will NOT appear. (Which kind of join should you use?)
SELECT
  p.id AS purchase_id,
  c.firstname,
  c.lastname,
  p.item_id,
  p.quantity_purchased
FROM purchases p
INNER JOIN customers c ON p.customer_id = c.id;