--Exercise 1: Building a Comprehensive Dataset for Employee Analysis

--1.Create a temporary table that join all tables and create a new one using LEFT JOIN.
CREATE TABLE emp_data_full AS
SELECT *
FROM salaries   s
LEFT JOIN company  c      ON s.comp_name    = c.company_name         
LEFT JOIN functions  f    ON s.func_code    = f.function_code       
LEFT JOIN employees  e    ON s.employee_id  = e.employee_code_emp;   
select * from emp_data_full;

--2.Create an unique identifier code between the columns ‘employee_id’ and ‘date’ and call it ‘id’.
--3.Convert the column ‘date’ to DATE type because it was previously configured as TIMESTAMP.
--4.Transform this new table into a dataset “df_employee” for analysis.

CREATE TABLE df_employee AS
SELECT 
    employee_id || '_' || CAST(date AS date) AS id,  
    DATE(date) AS month_year,
    employee_id, 
    employee_name_emp as employee_name, 
    gen_m_f_ as gender,  
    age,
    salary,
    function_group, 
    comp_name as company_name, 
    company_city, 
    company_state, 
    company_type, 
    const_site_category
FROM emp_data_full;


--Exercise 2: Cleaning Data for Consistency and Quality

--1. Run the following SQLite request and observe your new table.
select* from df_employee;

--2. Remove all unwanted spaces from all text columns using TRIM

UPDATE df_employee
SET
id = TRIM(id),
employee_name = TRIM(employee_name),
gender = TRIM(gender),
salary = TRIM(salary),
function_group = TRIM(function_group),
company_name = TRIM(company_name),
company_city = TRIM(company_city),
company_state = TRIM(company_state),
company_type = TRIM(company_type),
const_site_category	= TRIM(const_site_category);
select* from df_employee;

--3. Check for NULL values and empty values.

SELECT *
FROM df_employee
	WHERE id IS NULL
	OR month_year IS NULL
	OR employee_id IS NULL
	OR employee_name IS NULL
	OR gender IS NULL
	OR age IS NULL
	OR salary IS NULL
	OR function_group IS NULL
	OR company_name IS NULL
	OR company_city IS NULL
	OR company_state IS NULL
	OR company_type IS NULL
	OR const_site_category IS NULL;

SELECT *
	FROM df_employee
	WHERE id = ' '
	OR month_year = ' '
	OR employee_id = ' '
	OR employee_name = ' '
	OR gender = ' '
	OR age = ' '
	OR salary = ' '
	OR function_group = ' '
	OR company_name = ' '
	OR company_city = ' '
	OR company_state = ' '
	OR company_type = ' '
	OR const_site_category = ' ';

-- 4. Delete rows of the detected missing values.
DELETE FROM df_employee
WHERE salary = ' ';
DELETE FROM df_employee
WHERE const_site_category = ' ';

--Checking standardization
--id
SELECT DISTINCT id
FROM df_employee
GROUP BY id;

--gender
UPDATE df_employee
SET gender = CASE gender
				WHEN 'M' THEN 'Male'
				WHEN 'F' THEN 'Female'
				ELSE gender
			END
			
select * from df_employee;

--age
SELECT DISTINCT age
from df_employee
GROUP BY age
ORDER BY age;

--salary

DELETE FROM df_employee
WHERE salary = 1000000;
	
--function GROUP
select distinct function_group
from df_employee
GROUP BY function_group;


--Exercise 3 : Calculating Current Employee Counts by Company
select * from df_employee;
SELECT COUNT(DISTINCT employee_id) AS employees_today, company_name
FROM df_employee
WHERE month_year = (SELECT MAX(month_year) FROM df_employee)
GROUP BY company_name;

--Exercise 4 : Analyzing Employee Distribution by City and Over Time

-- Total number of employees per city + percentage
with city_counts as (
Select 
company_city,
COUNT (distinct employee_id) as total_employee
FROM df_employee
GROUP by company_city
)
SELECT 
company_city,
total_employee,
ROUND(100.0 * total_employee/ SUM(total_employee) OVER(), 2) as percentage
FROM city_counts
ORDER BY total_employee DESC;

-- Total and Average number of employees per month:

WITH monthly_counts AS (
  SELECT 
    TO_CHAR(TO_DATE(date, 'DD/MM/YYYY'), 'YYYY-MM') AS month_year,
    COUNT(DISTINCT employee_id) AS total_employees_per_month
  FROM salaries
  GROUP BY TO_CHAR(TO_DATE(date, 'DD/MM/YYYY'), 'YYYY-MM')
)
SELECT
  month_year,
  total_employees_per_month,
  ROUND(AVG(total_employees_per_month) OVER (), 0) AS avg_employees_per_month
FROM monthly_counts
ORDER BY month_year;

-- Exercise 5 : Analyzing Employment Trends and Salary Metrics
--Minimum and maximum number of employees throughout all the months.
WITH monthly_counts AS (
  SELECT 
    TO_CHAR(TO_DATE(date, 'DD/MM/YYYY'), 'YYYY-MM') AS month_year,
    COUNT(DISTINCT employee_id) AS total_employees_per_month
  FROM salaries
  GROUP BY TO_CHAR(TO_DATE(date, 'DD/MM/YYYY'), 'YYYY-MM')
)
SELECT
  month_year,
  total_employees_per_month
FROM monthly_counts
WHERE total_employees_per_month =(
	SELECT MIN(total_employees_per_month) FROM monthly_counts
	)
	OR total_employees_per_month =(
	SELECT MAX(total_employees_per_month) FROM monthly_counts
	)
ORDER BY total_employees_per_month DESC;

--Monthly average number of employees by function group
WITH monthly_fg AS (
  SELECT 
    TO_CHAR(TO_DATE(date, 'DD/MM/YYYY'), 'YYYY-MM') AS month_year,
    f.function_group,
	COUNT(DISTINCT employee_id) AS employee_per_month
  FROM salaries s 
  JOIN functions f
  ON s.func_code = f.function_code
  GROUP BY TO_CHAR(TO_DATE(date, 'DD/MM/YYYY'), 'YYYY-MM'),
  f.function_group
)
SELECT 
function_group,
ROUND(AVG(employee_per_month), 0) AS avg_employees_per_month
	
FROM monthly_fg
GROUP BY function_group
ORDER BY avg_employees_per_month DESC;

--Annual average salary
SELECT
  EXTRACT(YEAR FROM TO_DATE(date, 'DD/MM/YYYY')) AS year,
  ROUND(
    AVG(
      REPLACE(NULLIF(TRIM(salary), ''), ',', '.')::numeric
    ),
    2
  ) AS avg_salary
FROM salaries
GROUP BY 1
ORDER BY 1;


