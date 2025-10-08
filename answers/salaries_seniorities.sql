SELECT * FROM salaries
CROSS JOIN seniorities
WHERE salaries.employee_id = seniorities.employee_id
