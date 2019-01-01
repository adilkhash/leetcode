-- https://leetcode.com/problems/delete-duplicate-emails/

DELETE FROM Person
WHERE Id IN (
    SELECT
        p.Id
    FROM
        (SELECT * FROM Person) as p
    INNER JOIN (
        SELECT
            MIN(Id) as Id,
            Email
        FROM
            Person
        GROUP BY Email
        HAVING COUNT(1) > 1
    ) as t ON p.Email = t.Email AND p.Id > t.Id
)
