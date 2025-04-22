-- Please create column(s) first...


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


 -- Use SQL to fetch the following data from the database:

-- All the items.
SELECT * from items

-- All the items with a price above 80 (80 not included).
SELECT * from items WHERE price > 80;

-- All the items with a price below 300. (300 included)
SELECT * from items WHERE price <= 300;

-- All customers whose last name is ‘Smith’ (What will be your outcome?).
SELECT * from customers WHERE lastname = 'Smith';

-- All customers whose last name is ‘Jones’.
SELECT * from customers WHERE lastname = 'Jones';

--All customers whose firstname is not ‘Scott’.

SELECT * from customers WHERE firstname !=  'Scott';