--Exercise 1: Movie Rankings and Analysis

--Task_1_Rank Movies by Popularity within Each Genre

select title,genre_name,
RANK() OVER (PARTITION BY genre_name ORDER BY popularity DESC) AS rank
(
from movies.movie m 
join movies.movie_genres mg ON m.movie_id = mg.movie_id
join movies.genre g ON mg.genre_id =g.genre_id) as movies_by_genre
ORDER BY genre_name,rank,title;

--Task_2_ Identify the Top 3 Movies by Revenue within Each Production Company

SELECT pc.company_name, m.title, m.revenue,
NTILE(4) OVER (PARTITION BY pc.company_name ORDER BY m.revenue DESC) AS quartile
from movies.production_company pc
JOIN movies.movie_company mc ON pc.company_id = mc.company_id
JOIN movies.movie m ON mc.movie_id = m.movie_id
ORDER BY pc.company_name,quartile,m.revenue DESC

--Task 3: Calculate the Running Total of Movie Budgets for Each Genre

select g.genre_name,title, budget,
SUM(budget) OVER (PARTITION BY g.genre_name ORDER BY m.budget ROWS BETWEEN UNBOUNDED PRECEDING and CURRENT ROW ) AS running_total
from movies.movie m 
join movies.movie_genres mg ON m.movie_id = mg.movie_id
join movies.genre g ON mg.genre_id =g.genre_id
ORDER BY g.genre_name,m.budget

--Task 4: Identify the Most Recent Movie for Each Genre

select DISTINCT g.genre_name,
FIRST_VALUE(m.title) OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS most_recent_movie_released,
FIRST_VALUE(m.release_date) OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS release_date
FROM movies.movie m
join movies.movie_genres mg ON m.movie_id = mg.movie_id
join movies.genre g ON mg.genre_id =g.genre_id
ORDER BY g.genre_name

--Exercise 2: Cast and Crew Performance Analysis

--Task 1: Rank Actors by Their Appearance in Movies
select person_name,
COUNT(mc.movie_id) as movie_count,
DENSE_RANK() OVER (ORDER BY COUNT(mc.movie_id) DESC) AS actor_rank
From movies.person p
JOIN movies.movie_cast mc ON p.person_id = mc.person_id
GROUP BY p.person_name
ORDER BY actor_rank;

--Task 2: Identify the Top Director by Average Movie Rating

WITH director_avg AS (
    SELECT p.person_id,person_name,
	AVG(m.vote_average) as avg_rating
     
from movies.person p
JOIN movies.movie_crew mc ON p.person_id = mc.person_id
JOIN movies.movie m ON m.movie_id = mc.movie_id
JOIN movies.department d ON d.department_id = mc.department_id
WHERE d.department_name = 'Directing'
    AND (mc.job = 'Director' OR mc.job ILIKE '%Director%')		   
     GROUP BY p.person_id, p.person_name
),
ranked AS (
  SELECT
    person_name,
    avg_rating,
    RANK() OVER (ORDER BY avg_rating DESC) AS rnk
  FROM director_avg
)
SELECT
  person_name,
  ROUND(avg_rating::numeric, 2) AS avg_rating
FROM ranked
WHERE rnk = 1
ORDER BY person_name;


--Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor
WITH actors_movies AS (
SELECT DISTINCT 
p.person_id,p.person_name,m.movie_id,m.title,m.release_date,
COALESCE(m.revenue, 0) AS revenue
From movies.person p
JOIN movies.movie_cast mc ON p.person_id = mc.person_id
JOIN movies.movie m ON mc.movie_id = m.movie_id)
SELECT
  person_id,person_name,movie_id,title,release_date,revenue,
  SUM(revenue) OVER (
    PARTITION BY person_id
    ORDER BY release_date, movie_id
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS cumulative_revenue
FROM actors_movies
ORDER BY person_name, release_date, movie_id;

--Task 4: Identify the Director Whose Movies Have the Highest Total Budget

WITH director_movies AS (
  -- one row per (director, movie) to avoid double-counting
  SELECT DISTINCT
    p.person_id,
    p.person_name,
    m.movie_id,
    COALESCE(m.budget, 0) AS budget
  FROM movies.person p
  JOIN movies.movie_crew mc   ON mc.person_id = p.person_id
  JOIN movies.movie m         ON m.movie_id = mc.movie_id
  JOIN movies.department d    ON d.department_id = mc.department_id
  WHERE d.department_name = 'Directing'
    AND (mc.job = 'Director' OR mc.job ILIKE '%Director%')
),
director_totals AS (
  SELECT
    person_id,
    person_name,
    SUM(budget) AS total_budget
  FROM director_movies
  GROUP BY person_id, person_name
),
ranked AS (
  SELECT
    person_name,
    total_budget,
    RANK() OVER (ORDER BY total_budget DESC) AS rnk
  FROM director_totals
)
SELECT person_name, total_budget
FROM ranked
WHERE rnk = 1
ORDER BY person_name;

