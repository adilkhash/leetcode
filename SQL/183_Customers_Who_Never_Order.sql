-- https://leetcode.com/problems/customers-who-never-order/

SELECT
    Name as Customers
FROM (
    SELECT
        Name,
        o.Id as orderId
    FROM
        Customers as c
    LEFT JOIN Orders as o
    ON c.Id = o.CustomerId
) as o
WHERE orderId is NULL;
