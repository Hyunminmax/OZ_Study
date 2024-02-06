use sakila;
-- 데이터 조회 및 필터링
-- 1.
SELECT 
    film.title
FROM
    actor a
        JOIN
    film_actor fa ON a.actor_id = fa.actor_id
        JOIN
    film film ON fa.film_id = film.film_id
WHERE
    a.first_name = 'PENELOPE'
        AND a.last_name = 'GUINESS';

-- 2.
SELECT 
    c.name, COUNT(fc.film_id) AS film
FROM
    category c
        JOIN
    film_category fc ON c.category_id = fc.category_id
GROUP BY c.name;

-- 3.
select cus.first_name, cus.last_name, f.title, r.rental_date, r.return_date
from customer cus join rental r on cus.customer_id = r.customer_id
join inventory i on r.inventory_id = i.inventory_id
join film f on i.film_id = f.film_id
where cus.customer_id = 5;

-- 4. 
select title, release_year from film order by release_year DESC limit 10;

-- 조인 및 관계
-- 1.
SELECT 
    f.title, a.first_name, a.last_name
FROM
    actor a
        JOIN
    film_actor fa ON a.actor_id = fa.actor_id
        JOIN
    film f ON fa.film_id = f.film_id
WHERE
    f.title = 'ACADEMY DINOSAUR';

-- 2. 
SELECT 
    cus.first_name, cus.last_name
FROM
    customer cus
        JOIN
    rental r ON r.customer_id = cus.customer_id
        JOIN
    inventory i ON i.inventory_id = r.inventory_id
        JOIN
    film f ON f.film_id = i.film_id
WHERE
    f.title = 'ACADEMY DINOSAUR';

-- 3. 
SELECT 
    r.customer_id,
    cus.first_name,
    cus.last_name,
    f.title,
    MAX(r.rental_date)
FROM
    rental r
        JOIN
    customer cus ON cus.customer_id = r.customer_id
        JOIN
    inventory i ON i.inventory_id = r.inventory_id
        JOIN
    film f ON f.film_id = i.film_id
GROUP BY r.customer_id, cus.first_name, cus.last_name, f.title;

-- 4. 

SELECT 
    f.title, AVG(DATEDIFF(r.return_date, r.rental_date))
FROM
    rental r
        JOIN
    inventory i ON i.inventory_id = r.inventory_id
        JOIN
    film f ON f.film_id = i.film_id
GROUP BY r.inventory_id;

-- 집계 및 그룹화
-- 1.
SELECT 
    f.title, COUNT(r.rental_id) 
FROM
    film f
        JOIN
    inventory i ON f.film_id = i.film_id
        JOIN
    rental r ON i.inventory_id = r.inventory_id
GROUP BY f.title
ORDER BY rental_count DESC
LIMIT 1;

-- 2.
SELECT 
    c.name, AVG(f.rental_rate)
FROM
    category c
        JOIN
    film_category fc ON c.category_id = fc.category_id
        JOIN
    film f ON fc.film_id = f.film_id
GROUP BY c.name;

-- 3.
SELECT 
    YEAR(p.payment_date) AS year,
    MONTH(p.payment_date) AS month,
    SUM(p.amount)
FROM
    payment p
GROUP BY YEAR(p.payment_date) , MONTH(p.payment_date);

-- 4.
SELECT 
    a.first_name,
    a.last_name,
    COUNT(fa.film_id) 
FROM
    actor a
        JOIN
    film_actor fa ON a.actor_id = fa.actor_id
GROUP BY a.first_name , a.last_name;

-- 서브쿼리 및 고급 기능
-- 1.
SELECT 
    f.title, SUM(p.amount)
FROM
    film f
        JOIN
    inventory i ON f.film_id = i.film_id
        JOIN
    rental r ON i.inventory_id = r.inventory_id
        JOIN
    payment p ON r.rental_id = p.rental_id
GROUP BY f.title
ORDER BY SUM(p.amount) DESC
LIMIT 1;

-- 2. 
SELECT 
    f.title, f.rental_rate
FROM
    film f
WHERE
    f.rental_rate > (SELECT 
            AVG(rental_rate)
        FROM
            film);
            
-- 3.
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(r.rental_id) 
FROM
    rental r
        JOIN
    customer c ON r.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY COUNT(r.rental_id) DESC
LIMIT 1;

-- 4. 
SELECT 
    f.title, COUNT(r.rental_id)
FROM
    film f
        JOIN
    film_actor fa ON f.film_id = fa.film_id
        JOIN
    actor a ON fa.actor_id = a.actor_id
        JOIN
    inventory i ON f.film_id = i.film_id
        JOIN
    rental r ON i.inventory_id = r.inventory_id
WHERE
    a.first_name = 'PENELOPE'
        AND a.last_name = 'GUINESS'
GROUP BY f.title
ORDER BY COUNT(r.rental_id) DESC
LIMIT 1;

-- 데이터 수정 및 관리
-- 1.
update language set name = '한국어' where language_id = 1;
INSERT INTO film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features)
VALUES ('New Adventure Movie', '엑설런트어드밴쳐 보다 재미있는 뉴 어드밴쳐', 2024, 1, 2, 4.99, 90, 180, 'G', 'Commentaries,Deleted Scenes');
-- 2.
UPDATE customer
SET address_id = (SELECT address_id FROM address WHERE address = '123 New Address, New City')
WHERE customer_id = 5;
-- 3.
UPDATE rental
SET return_date = NOW()
WHERE rental_id = 200;
-- 4.
DELETE FROM actor
WHERE actor_id = 10;


select * from language;
select * from customer;
select * from rental;
select * from inventory;
select * from category;
select * from film_category;
select * from actor;
select * from film;
select * from film_actor;