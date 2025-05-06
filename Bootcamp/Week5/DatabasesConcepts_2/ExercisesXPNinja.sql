--Exercise 1 : DVD Rentals
--Instructions
--
--We want to encourage families and kids to enjoy our movies.

 --   Retrieve all films with a rating of G or PG, which are are not currently rented (they have been returned/have never been borrowed).
SELECT DISTINCT f.film_id, f.title, f.rating FROM film f
JOIN inventory i ON f.film_id = i.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
WHERE f.rating IN ('G', 'PG')
  AND (r.return_date IS NOT NULL OR r.rental_id IS NULL);

--  Create a new table which will represent a waiting list for children’s movies. This will allow a child to add their name to the list until the DVD is available (has been returned). Once the child takes the DVD, their name should be removed from the waiting list (ideally using triggers, but we have not learned about them yet. Let’s assume that our Python program will manage this). Which table references should be included?
CREATE TABLE waiting_list_kids (
    id SERIAL PRIMARY KEY,
    child_name VARCHAR(100) NOT NULL,
    film_id INT NOT NULL REFERENCES film(film_id) ON DELETE CASCADE,
    added_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Retrieve the number of people waiting for each children’s DVD. Test this by adding rows to the table that you created in question 2 above.
SELECT f.title, COUNT(k.id) AS people_waiting
FROM waiting_list_kids k
JOIN film f ON k.film_id = f.film_id
WHERE f.rating IN ('G', 'PG')
GROUP BY f.title
ORDER BY people_waiting DESC;
