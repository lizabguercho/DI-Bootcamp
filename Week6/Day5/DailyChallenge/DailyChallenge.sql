--Task_1 Calculate the Average Budget Growth Rate for Each Production Company
--1)List each company's movies with their budget and the previous movie's budget
WITH company_movies AS (
  SELECT
    pc.company_name,
    m.movie_id,
    m.release_date,
    m.budget,
    LAG(m.budget) OVER (
      PARTITION BY pc.company_name
      ORDER BY m.release_date, m.movie_id   -- chronological, tie-break by id
    ) AS prev_budget
  FROM movies.production_company pc
  JOIN movies.movie_company mc ON mc.company_id = pc.company_id
  JOIN movies.movie m          ON m.movie_id = mc.movie_id
)

-- 2) For each company, average the movie-to-movie growth rates
SELECT
  company_name,
  ROUND(
    AVG(
      CASE
        WHEN prev_budget IS NULL OR prev_budget = 0 OR budget IS NULL
          THEN NULL                         -- skip first movie / bad data
        ELSE (budget - prev_budget)::numeric / prev_budget
      END
    )::numeric
  , 4) AS avg_budget_growth_rate
FROM company_movies
GROUP BY company_name
ORDER BY avg_budget_growth_rate DESC NULLS LAST, company_name;

--Task 2: Determine the Most Consistently High-Rated Actor
WITH movie_with_global_avg AS (
  SELECT
    m.movie_id,
    m.vote_average,
    AVG(m.vote_average) OVER () AS global_avg         -- window: average across all movies
  FROM movies.movie m
),
actor_movies AS (
  SELECT DISTINCT
    p.person_id,
    p.person_name,
    mwga.movie_id,
    mwga.vote_average,
    mwga.global_avg
  FROM movies.person p
  JOIN movies.movie_cast mc ON mc.person_id = p.person_id
  JOIN movie_with_global_avg mwga ON mwga.movie_id = mc.movie_id
  WHERE mwga.vote_average IS NOT NULL                 -- ignore unrated movies
),
above_avg_counts AS (
  SELECT
    person_id,
    person_name,
    COUNT(*) AS above_avg_movie_count
  FROM actor_movies
  WHERE vote_average > global_avg                     -- strictly above the global avg
  GROUP BY person_id, person_name
),
ranked AS (
  SELECT
    person_name,
    above_avg_movie_count,
    RANK() OVER (ORDER BY above_avg_movie_count DESC) AS rnk
  FROM above_avg_counts
)
SELECT
  person_name,
  above_avg_movie_count
FROM ranked
WHERE rnk = 1
ORDER BY person_name;

-- Task 3: Calculate the Rolling Average Revenue for Each Genre

WITH genre_movies AS (
  SELECT
    g.genre_name,
    m.movie_id,
    m.title,
    m.release_date,
    m.revenue
  FROM movies.movie m
  JOIN movies.movie_genres mg ON mg.movie_id = m.movie_id
  JOIN movies.genre g        ON g.genre_id = mg.genre_id
)
SELECT
  genre_name,
  title,
  release_date,
  revenue,
  AVG(revenue) OVER (
    PARTITION BY genre_name
    ORDER BY release_date NULLS LAST, movie_id
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
  ) AS rolling_avg_rev_last3
FROM genre_movies
ORDER BY genre_name, release_date NULLS LAST, movie_id;


--Task 4: Identify the Highest-Grossing Movie Series

-- 1) Get each (keyword = series, movie) with its revenue
WITH series_movies AS (
  SELECT DISTINCT
    k.keyword_id,
    k.keyword_name AS series_name,
    m.movie_id,
    COALESCE(m.revenue, 0) AS revenue
  FROM movies.movie m
  JOIN movies.movie_keywords mk ON mk.movie_id = m.movie_id
  JOIN movies.keyword k        ON k.keyword_id = mk.keyword_id
),

-- 2) For each series, compute the total revenue (as a window sum)
series_totals AS (
  SELECT
    keyword_id,
    series_name,
    SUM(revenue) OVER (PARTITION BY keyword_id) AS total_revenue
  FROM series_movies
),

-- 3) Keep one row per series and rank by total revenue
ranked_series AS (
  SELECT DISTINCT
    series_name,
    total_revenue,
    RANK() OVER (ORDER BY total_revenue DESC) AS rnk
  FROM series_totals
)

-- 4) Highest-grossing series (ties included)
SELECT
  series_name,
  total_revenue
FROM ranked_series
WHERE rnk = 1
ORDER BY series_name;