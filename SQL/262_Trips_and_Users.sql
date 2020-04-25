-- https://leetcode.com/problems/trips-and-users/

SELECT
    Day,
    ROUND((SUM(CASE WHEN Status IN ('cancelled_by_driver', 'cancelled_by_client') THEN Total_Rides ELSE 0 END))/ SUM(Total_Rides), 2) as "Cancellation Rate"
FROM (
SELECT
    Request_At as Day,
    clients.Status,
    COUNT(1) as Total_rides
FROM (

    SELECT
        Id,
        Banned as Client_Banned,
        Status,
        Request_at
    FROM
        Trips
    LEFT JOIN Users U ON U.Users_Id = Trips.Client_Id
) clients
JOIN (
SELECT
        Id,
        Banned as Driver_Banned,
        Status
    FROM
        Trips
    LEFT JOIN Users U ON U.Users_Id = Trips.Driver_Id

) drivers using(Id)
WHERE Client_Banned = 'No' AND Driver_Banned = 'No'
AND Request_at >= '2013-10-01'
AND Request_at < '2013-10-04'
GROUP BY 1,2
) cancelation_rates
GROUP BY 1
ORDER BY 1;
