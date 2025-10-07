--Exercise_1:Complex Subquery Analysis
-- Task_1
select 
m.medal_name,
(
select ROUND(AVG(gc.age *1.0),2)
from olympics.games_competitor gc
where exists (
  select 1
  from olympics.competitor_event ce
  where ce.competitor_id = gc.id
  and ce.medal_id =m.id) 
 ) as avg_age
 
 from olympics.medal m
 where m.medal_name <> 'NA'
 ORDER by m.medal_name;


--TASK_2
SELECT nr.region_name,
COUNT(DISTINCT pr.person_id) as unique_competitors
FROM olympics.noc_region nr
JOIN olympics.person_region pr
ON pr.region_id = nr.id
WHERE pr.person_id IN(
	SELECT DISTINCT gc.person_id
	FROM olympics.games_competitor gc
	WHERE gc.id IN(
		SELECT ce.competitor_id
		FROM olympics.competitor_event ce
		GROUP BY ce.competitor_id
		HAVING COUNT(Distinct ce.event_id)>3
	)
)
GROUP BY nr.region_name
ORDER BY unique_competitors DESC 
LIMIT 5;


SELECT * FROM olympics.competitor_event;

--TASK3	
-- Recreate temp table if needed
DROP TABLE IF EXISTS local_temp_table;
CREATE TEMP TABLE local_temp_table (
  id     INT PRIMARY KEY,  -- competitor_id
  medals INT NOT NULL
);
select * from local_temp_table;

ALTER TABLE local_temp_table
DROP COLUMN events;


-- Aggregate once, filter >2, then insert
INSERT INTO local_temp_table (id, medals)
SELECT ce.competitor_id AS id,
       COUNT(*) AS medals
FROM olympics.competitor_event ce
JOIN olympics.medal m
  ON m.id = ce.medal_id
WHERE m.medal_name <> 'NA'      -- count only real medals
GROUP BY ce.competitor_id
HAVING COUNT(*) > 2;            -- keep only competitors with > 2 medals
select * from local_temp_table;

-- If you want to see the results:
SELECT id AS competitor_id, medals
FROM local_temp_table
ORDER BY medals DESC;	


--TASK_4
DELETE FROM local_temp_table
WHERE id NOT IN (
SELECT DISTINCT ce.competitor_id 
FROM olympics.competitor_event ce
JOIN olympics.medal m
  ON m.id = ce.medal_id
WHERE m.medal_name <> 'NA'
)


--Exercise_2:Advanced Data Manipulation and Optimization

--TASK_1
UPDATE person p
SET p.height = (
	SELECT AVG(p2.height)  
	FROM person p2
	JOIN person_region pr2 ON pr2.person_id = p2.id
	JOIN person_region pr ON pr.person_id= p.id
	WHERE p2.height IS NOT NULL
)
WHERE EXISTS (SELECT 1 FROM person_region pr WHERE pr.person_id = p.id)

--TASK_2
DROP TABLE IF EXISTS local_temp_table2;
CREATE TEMP TABLE local_temp_table2 (
  games_id INT PRIMARY KEY,  -- competitor_id
  multi_competitor_count INT NOT NULL
);
INSERT INTO local_temp_table2 (games_id,multi_competitor_count )
SELECT games_id,count(competitor_id) as multi_competitor_count
FROM (SELECT ce.competitor_id, gc.games_id, count(ce.event_id) as event_total FROM olympics.competitor_event ce
JOIN olympics.games_competitor gc ON ce.competitor_id = gc.id
GROUP BY gc.games_id, ce.competitor_id 
HAVING COUNT (event_id)>1) as event_grouped
GROUP BY event_grouped.games_id;
select * from local_temp_table2;

-- TASK_3
-- Per-competitor medal counts (count only real medals; include zero-medal competitors)
WITH per_competitor AS (
  SELECT
    nc.region_name,
    gc.id AS competitor_id,
    SUM(CASE WHEN m.medal_name <> 'NA' THEN 1 ELSE 0 END) AS total_medals
  FROM olympics.noc_region nc
  JOIN olympics.person_region pr ON pr.region_id = nc.id
  JOIN olympics.games_competitor gc ON gc.person_id = pr.person_id
  LEFT JOIN olympics.competitor_event ce ON ce.competitor_id = gc.id
  LEFT JOIN olympics.medal m  ON m.id = ce.medal_id
  GROUP BY nc.region_name, gc.id
),

-- Average per region
region_avg AS (
  SELECT region_name, AVG(total_medals) AS avg_medals
  FROM per_competitor
  GROUP BY region_name
)

--  Keep regions above the overall average
SELECT
  region_name,
  ROUND(avg_medals, 2) AS avg_medal_won
FROM region_avg
WHERE avg_medals > (
  SELECT AVG(total_medals) FROM per_competitor
)
ORDER BY avg_medal_won DESC;



--TASK_4
DROP TABLE IF EXISTS tmp_competitor_seasons;
CREATE TEMP TABLE tmp_competitor_seasons AS
SELECT gc.id as competitor_id,g.season
FROM olympics.games_competitor gc
JOIN olympics.games g ON gc.games_id = g.id
JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id;

select competitor_id, count(season) as season_count
from tmp_competitor_seasons
Group By competitor_id
HAVING COUNT(*) = 2;


