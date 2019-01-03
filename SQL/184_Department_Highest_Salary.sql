-- https://leetcode.com/problems/department-highest-salary/

SELECT
    d.Name as Department,
    s.Employee,
    s.Salary
FROM (
    SELECT
        e.DepartmentId as DepartmentId,
        e.Name as Employee,
        t.Salary
    FROM
        Employee as e
    INNER JOIN (
        SELECT
            MAX(Salary) as Salary,
            DepartmentId
        FROM
            Employee
        GROUP BY
            DepartmentId
    ) as t
        ON e.DepartmentId = t.DepartmentId
        AND e.Salary = t.Salary
) as s
    INNER JOIN Department as d
        ON d.Id = s.DepartmentId
