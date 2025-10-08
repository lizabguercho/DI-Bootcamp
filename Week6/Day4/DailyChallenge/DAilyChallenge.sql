-- Exercise 1: Detailed Medal Analysis
--TASK_1 
DROP TABLE IF EXISTS tmp_both_seasons_medalists;

CREATE TEMP TABLE tmp_both_seasons_medalists AS
WITH counts AS (
  SELECT
    gc.person_id,
    SUM(CASE WHEN g.season = 'Summer' AND ce.medal_id IS NOT NULL THEN 1 ELSE 0 END) AS summer_medals,
    SUM(CASE WHEN g.season = 'Winter' AND ce.medal_id IS NOT NULL THEN 1 ELSE 0 END) AS winter_medals
  FROM olympics.games_competitor gc
  JOIN olympics.games g ON g.id = gc.games_id
  LEFT JOIN olympics.competitor_event ce ON ce.competitor_id = gc.id
  GROUP BY gc.person_id
)
SELECT person_id, summer_medals, winter_medals
FROM counts
WHERE summer_medals > 0 AND winter_medals > 0;

-- Show results (with names if you have them)
SELECT t.person_id, p.full_name, t.summer_medals, t.winter_medals
FROM tmp_both_seasons_medalists t
LEFT JOIN olympics.person p ON p.id = t.person_id
ORDER BY (t.summer_medals + t.winter_medals) DESC, t.person_id;

--TASK_2
DROP TABLE IF EXISTS tmp_two_sport_medalists;

CREATE TEMP TABLE tmp_two_sport_medalists AS
WITH per_person_sport AS (
  SELECT
    gc.person_id,
    e.sport_id,
    COUNT(*) AS medals_in_sport
  FROM olympics.games_competitor gc
  JOIN olympics.competitor_event ce ON ce.competitor_id = gc.id
  JOIN olympics.event e             ON e.id = ce.event_id
  LEFT JOIN olympics.medal m        ON m.id = ce.medal_id
  -- Count only real medals:
  WHERE ce.medal_id IS NOT NULL
    AND (m.medal_name IS NULL OR m.medal_name <> 'NA')
  GROUP BY gc.person_id, e.sport_id
),
per_person AS (
  SELECT
    person_id,
    COUNT(DISTINCT sport_id) AS sport_count,
    SUM(medals_in_sport)     AS total_medals
  FROM per_person_sport
  GROUP BY person_id
)
SELECT person_id, sport_count, total_medals
FROM per_person
WHERE sport_count = 2;   -- exactly two different sports

SELECT *
FROM tmp_two_sport_medalists
ORDER BY total_medals DESC, person_id;

--TOP3 competitors
SELECT *
FROM tmp_two_sport_medalists
WHERE person_id IN (
  SELECT person_id
  FROM tmp_two_sport_medalists
  ORDER BY total_medals DESC, person_id
  LIMIT 3
)

--Exercise 2: Region and Competitor Performance
--Task_1
DROP TABLE IF EXISTS tmp_max_medals_per_event_region;

CREATE TEMP TABLE tmp_max_medals_per_event_region AS
WITH person_region_unique AS (
  -- one (person_id, region_name) per person to avoid double-counting
  SELECT DISTINCT pr.person_id, nc.region_name
  FROM olympics.person_region pr
  JOIN olympics.noc_region  nc ON nc.id = pr.region_id
),
per_person_event AS (
  -- medals per (person, event)
  SELECT
    gc.person_id,
    ce.event_id,
    COUNT(*) AS medals_in_event
  FROM olympics.games_competitor gc
  JOIN olympics.competitor_event ce ON ce.competitor_id = gc.id
  LEFT JOIN olympics.medal m        ON m.id = ce.medal_id
  WHERE ce.medal_id IS NOT NULL                -- NULL-encoding of “no medal”
    AND (m.medal_name IS NULL OR m.medal_name <> 'NA')  -- 'NA'-encoding safe
  GROUP BY gc.person_id, ce.event_id
),
per_person_max AS (
  -- subquery: each person's maximum medals in any single event
  SELECT person_id, MAX(medals_in_event) AS max_medals_in_event
  FROM per_person_event
  GROUP BY person_id
),
best_events AS (
  -- keep the event(s) where the person hit their maximum (ties kept)
  SELECT ppe.person_id, ppe.event_id, ppe.medals_in_event AS max_medals_in_event
  FROM per_person_event ppe
  JOIN per_person_max  ppm
    ON ppm.person_id = ppe.person_id
   AND ppm.max_medals_in_event = ppe.medals_in_event
)
-- temp table contents: region + each person's best event and its medal count
SELECT
  pru.region_name,
  be.person_id,
  be.event_id,
  be.max_medals_in_event
FROM best_events be
JOIN person_region_unique pru ON pru.person_id = be.person_id;

SELECT *
FROM tmp_max_medals_per_event_region
ORDER BY max_medals_in_event DESC, region_name, person_id, event_id;

-- TOP 5 regions
SELECT
  region_name,
  SUM(max_medals_in_event) AS total_max_medals
FROM tmp_max_medals_per_event_region
GROUP BY region_name
ORDER BY total_max_medals DESC, region_name
LIMIT 5;


--Task_2
-- Recreate the temp table
DROP TABLE IF EXISTS tmp_no_medals_4plus_games;

CREATE TEMP TABLE tmp_no_medals_4plus_games AS
WITH per_person AS (
  SELECT
    gc.person_id,
    COUNT(DISTINCT gc.games_id) AS games_participated,
    -- Count real medals (works for NULL- or 'NA'-style schemas)
    SUM(CASE WHEN ce.medal_id IS NOT NULL
             AND (m.medal_name IS NULL OR m.medal_name <> 'NA')THEN 1 ELSE 0 END) AS medals_won
  FROM olympics.games_competitor gc
  LEFT JOIN olympics.competitor_event ce ON ce.competitor_id = gc.id
  LEFT JOIN olympics.medal m             ON m.id = ce.medal_id
  GROUP BY gc.person_id
)
SELECT person_id, games_participated
FROM per_person
WHERE games_participated > 3              -- participated in more than 3 Games
  AND COALESCE(medals_won, 0) = 0;        -- but won no medals

SELECT
  t.person_id,
  p.full_name,
  t.games_participated
FROM tmp_no_medals_4plus_games t
JOIN olympics.person p ON p.id = t.person_id
ORDER BY t.games_participated DESC, p.full_name, t.person_id;

