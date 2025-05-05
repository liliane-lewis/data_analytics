--Exercise 1 : DVD Rentals
--Instructions

--    Get a list of all rentals which are out (have not been returned). How do we identify these films in the database?
SELECT * FROM rental WHERE return_date IS NULL;

--    Get a list of all customers who have not returned their rentals. Make sure to group your results.
SELECT 
  c.customer_id,
  c.first_name,
  c.last_name,
  COUNT(r.rental_id) AS unreturned_rentals
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
WHERE r.return_date IS NULL
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY unreturned_rentals DESC;

--    Get a list of all the Action films with Joe Swank.
--        Before you start, could there be a shortcut to getting this information? Maybe a view?

SELECT DISTINCT f.title
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE c.name = 'Action'
  AND a.first_name = 'Joe'
  AND a.last_name = 'Swank';


--Exercise 2 – Happy Halloween
--Instructions

--There is a zombie plague approaching! The DVD rental company is offering to lend all of its DVDs to the local shelters, so that the citizens can watch the movies together in the shelters until the zombies are destroyed by the armed forces. Prepare tables with the following data:
--
--   How many stores there are, and in which city and country they are located.
SELECT 
  s.store_id,
  ci.city,
  co.country
FROM store s
JOIN address a ON s.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id;


-- How many hours of viewing time there are in total in each store – in other words, the sum of the length of every inventory item in each store.
-- Make sure to exclude any inventory items which are not yet returned. (Yes, even in the time of zombies there are people who do not return their DVDs)

SELECT 
  s.store_id,
  SUM(f.length) AS total_minutes,
  ROUND(SUM(f.length) / 60.0, 2) AS total_hours,
  ROUND(SUM(f.length) / 60.0 / 24.0, 2) AS total_days
FROM store s
JOIN inventory i ON s.store_id = i.store_id
JOIN film f ON i.film_id = f.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NOT NULL
GROUP BY s.store_id;


-- A list of all customers in the cities where the stores are located.
SELECT DISTINCT c.*
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
WHERE ci.city_id IN (
    SELECT ci.city_id
    FROM store s
    JOIN address a ON s.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
);

-- A list of all customers in the countries where the stores are located.
SELECT DISTINCT c.*
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE co.country_id IN (
    SELECT co.country_id
    FROM store s
    JOIN address a ON s.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
    JOIN country co ON ci.country_id = co.country_id
);


--Some people will be frightened by watching scary movies while zombies walk the streets. 
    
    --Create a ‘safe list’ of all movies which do not include the ‘Horror’ category, or contain the words ‘beast’, ‘monster’, ‘ghost’, ‘dead’, ‘zombie’,'
    -- or ‘undead’ in their titles or descriptions… Get the sum of their viewing time (length).
    --Hint : use the CHECK contraint
SELECT 
  COUNT(*) AS safe_movie_count,
  SUM(f.length) AS total_minutes,
  ROUND(SUM(f.length)/60.0, 2) AS total_hours,
  ROUND(SUM(f.length)/60.0/24.0, 2) AS total_days
FROM film f
LEFT JOIN film_category fc ON f.film_id = fc.film_id
LEFT JOIN category c ON fc.category_id = c.category_id
WHERE (c.name IS DISTINCT FROM 'Horror')
  AND f.title NOT ILIKE ANY (ARRAY[
    '%beast%', '%monster%', '%ghost%', '%dead%', '%zombie%', '%undead%'
  ])
  AND f.description NOT ILIKE ANY (ARRAY[
    '%beast%', '%monster%', '%ghost%', '%dead%', '%zombie%', '%undead%'
  ]);

    --For both the ‘general’ and the ‘safe’ lists above, also calculate the time in hours and days (not just minutes).
SELECT 
  COUNT(*) AS total_movies,
  SUM(length) AS total_minutes,
  ROUND(SUM(length)/60.0, 2) AS total_hours,
  ROUND(SUM(length)/60.0/24.0, 2) AS total_days
FROM film;

