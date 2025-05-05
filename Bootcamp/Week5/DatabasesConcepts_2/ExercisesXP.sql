--  Exercises XP

--Exercise 1: DVD Rental
--Instructions

--    Get a list of all the languages, from the language table.
SELECT name FROM language;

--Get a list of all films joined with their languages – select the following details : film title, description, and language name.

SELECT 
    f.title,
    f.description,
    l.name AS language_name
FROM film f
INNER JOIN language l ON f.language_id = l.language_id;


--    Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
SELECT 
    f.title,
    f.description,
    l.name AS language_name
FROM language l
LEFT JOIN film f ON f.language_id = l.language_id;

--Create a new table called new_film with the following columns : id, name. Add some new films to the table.

CREATE TABLE new_film (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100)
);

INSERT INTO new_film (name) VALUES
('The Godfather'),
('The Matrix');

-- Create a new table called customer_review, which will contain film reviews that customers will make.
--    Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
--   It should have the following columns:
--        review_id – a primary key, non null, auto-increment.
--        film_id – references the new_film table. The film that is being reviewed.
--        language_id – references the language table. What language the review is in.
--        title – the title of the review.
--        score – the rating of the review (1-10).
--        review_text – the text of the review. No limit on the length.
--        last_update – when the review was last updated.
CREATE TABLE customer_review (
  review_id SERIAL PRIMARY KEY,
  film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
  language_id INT REFERENCES language(language_id),
  title VARCHAR(255),
  score INT CHECK (score BETWEEN 1 AND 10),
  review_text TEXT,
  last_update TIMESTAMP
);

--Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES
(1, 1, 'Amazing movie', 9, 'A masterpiece of sci-fi!', NOW()),
(2, 2, 'Great action', 8, 'Explosive scenes and deep plot.', NOW());

--Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film WHERE id = 1;


--Exercise 2 : DVD Rental
--Instructions

--Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film SET language_id = 2 WHERE film_id IN (1, 2, 3);
    
--Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?

SELECT 
    tc.constraint_name, 
    kcu.column_name, 
    ccu.table_name AS foreign_table,
    ccu.column_name AS foreign_column
FROM information_schema.table_constraints AS tc
JOIN information_schema.key_column_usage AS kcu 
  ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage AS ccu 
  ON ccu.constraint_name = tc.constraint_name
WHERE tc.table_name = 'customer' AND tc.constraint_type = 'FOREIGN KEY';

--We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE customer_review;

--Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT COUNT(*) AS outstanding_rentals FROM rental WHERE return_date IS NULL;


--Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT f.title, f.rental_rate
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.rental_rate DESC
LIMIT 30;

--Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him 
-- find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'Penelope' AND a.last_name = 'Monroe'
  AND f.description ILIKE '%sumo%';

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT title FROM film WHERE length < 60 AND rating = 'R';

--The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN payment p ON r.rental_id = p.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
  AND p.amount > 4.00
  AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
SELECT f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC
LIMIT 1;