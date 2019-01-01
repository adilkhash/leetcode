-- https://leetcode.com/problems/employees-earning-more-than-their-managers/

SELECT
    Name as Employee
FROM
    Employee as e
INNER JOIN
(
    SELECT
        Id,
        Salary
    FROM Employee
) as m
ON m.Id = e.ManagerId
AND e.Salary > m.Salary;
