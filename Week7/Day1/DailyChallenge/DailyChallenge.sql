CREATE TABLE employees1 (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date VARCHAR(20),
    department VARCHAR(50)
);
INSERT INTO employees1 (employee_id, employee_name, salary, hire_date, department) VALUES
(1, 'Amy West', 60000.00, '2021-01-15', 'HR'),
(2, 'Ivy Lee', 75000.50, '2020-05-22', 'Sales'),
(3, 'joe smith', 80000.75, '2019-08-10', 'Marketing'), 
(4, 'John White', 90000.00, '2020-11-05', 'Finance'),
(5, 'Jane Hill', 55000.25, '2022-02-28', 'IT'),
(6, 'Dave West', 72000.00, '2020-03-12', 'Marketing'),
(7, 'Fanny Lee', 85000.50, '2018-06-25', 'Sales'),
(8, 'Amy Smith', 95000.25, '2019-11-30', 'Finance'),
(9, 'Ivy Hill', 62000.75, '2021-07-18', 'IT'),
(10, 'Joe White', 78000.00, '2022-04-05', 'Marketing'),
(11, 'John Lee', 68000.50, '2018-12-10', 'HR'),
(12, 'Jane West', 89000.25, '2017-09-15', 'Sales'),
(13, 'Dave Smith', 60000.75, '2022-01-08', NULL),
(14, 'Fanny White', 72000.00, '2019-04-22', 'IT'),
(15, 'Amy Hill', 84000.50, '2020-08-17', 'Marketing'),
(16, 'Ivy West', 92000.25, '2021-02-03', 'Finance'),
(17, 'Joe Lee', 58000.75, '2018-05-28', 'IT'),
(18, 'John Smith', 77000.00, '2019-10-10', 'HR'),
(19, 'Jane Hill', 81000.50, '2022-03-15', 'Sales'),
(20, 'Dave White', 70000.25, '2017-12-20', 'Marketing');

select * from employees1;
--1. Check for missing values in the table
SELECT
count(*) as total_rows,
count(*) - count(employee_id) as missing_employee_id,
count(*) - count(employee_name) as missing_name,
count(*) - count(salary) as missing_salary,
count(*) - count (hire_date) as missing_hire_date,
count(*) - count (department) as missing_department
from employees1;

-- replace missing VALUE
UPDATE employees1
SET department = 'Uknown'
Where department IS NULL;

--2.Check for and eliminate any duplicate rows in the dataset.

SELECT
  *,
  COUNT(*) AS n
FROM employees1
GROUP BY
  employee_id,employee_name, salary, hire_date, department -- list all columns
HAVING COUNT(*) > 1
ORDER BY n DESC;

--3.Correct any structural issues, such as inconsistent naming conventions or formatting errors.
UPDATE employees1
SET employee_name = 'Joe Smith'
Where employee_name = 'joe smith';

select * from employees1;

--4.Ensure all columns have appropriate data types (e.g. the hire_date column).
-- check data type in each column
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'employees1';

-- convert column "hire_date" to a date data type
ALTER TABLE employees1
ALTER COLUMN hire_date TYPE DATE 
USING hire_date:: DATE;

--5.Detect and address any outliers that may skew the analysis.

--IQR rule to detect outliers
WITH q AS (
  SELECT
    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY salary) AS q1,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY salary) AS q3
  FROM employees1
),
b AS (
  SELECT q1, q3,
         q1 - 1.5*(q3-q1) AS lb,
         q3 + 1.5*(q3-q1) AS ub
  FROM q
)
SELECT e.*,
       (e.salary < b.lb OR e.salary > b.ub) AS is_outlier
FROM employees1 e CROSS JOIN b
ORDER BY salary;

--6.Standardize and normalize data where applicable to ensure consistency.
--remove spaces 
UPDATE employees1
SET employee_name = TRIM(employee_name);

CREATE TABLE departments (
  department_id SERIAL PRIMARY KEY,
  department_name VARCHAR(50) UNIQUE NOT NULL
);

-- Seed from existing values
INSERT INTO departments (department_name)
SELECT DISTINCT department
FROM employees1
ORDER BY 1;

-- Add FK column and backfill
ALTER TABLE employees1 ADD COLUMN department_id INT;

UPDATE employees1 e
SET department_id = d.department_id
FROM departments d
WHERE e.department = d.department_name;

-- Enforce the relationship
ALTER TABLE employees1
  ADD CONSTRAINT employees1_department_fk
  FOREIGN KEY (department_id) REFERENCES departments(department_id);

select * from employees1;

