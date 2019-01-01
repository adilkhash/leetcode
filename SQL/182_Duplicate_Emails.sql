-- https://leetcode.com/problems/duplicate-emails

SELECT Email FROM (
    SELECT
        Email,
        COUNT(1)
    FROM Person
    GROUP BY Email
    HAVING COUNT(1) > 1
) AS d;
