SELECT salary, salaries.employee_id, seniority
FROM salaries
INNER JOIN seniorities
ON salaries.employee_id = seniorities.employee_id