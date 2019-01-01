-- https://leetcode.com/problems/rising-temperature/

SELECT
    Id
FROM (
    SELECT
        w.Id,
        w.RecordDate,
        w.Temperature,
        w.Temperature - t.Temperature as TemperatureDiff
    FROM Weather as w JOIN
        (
            SELECT
                Id,
                RecordDate,
                Temperature,
                DATE_SUB(RecordDate, INTERVAL 1 DAY) as PrevDate
            FROM Weather
        ) as t
    ON DATE_SUB(w.RecordDate, INTERVAL 1 DAY) = t.RecordDate
) as r
WHERE r.TemperatureDiff > 0
