SELECT
    s.Score,
    t.Rank
FROM Scores s
JOIN (
    SELECT
        Score,
        @n := @n + 1 Rank
    FROM (
        SELECT
            DISTINCT Score
        FROM Scores
        ORDER BY Score DESC
    ) as t, (SELECT @n := 0) as m
) as t
ON s.Score = t.Score
ORDER BY Rank;
