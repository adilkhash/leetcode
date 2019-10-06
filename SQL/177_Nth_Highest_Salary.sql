CREATE FUNCTION getNthHighestSalary (@N INT) RETURNS INT AS
BEGIN
RETURN
(
    /* Write your T-SQL query statement below. */
    select Salary
    from (
             select Salary,
                    dense_rank() over (order by Salary desc) rank
             from Employee
         ) as t
    where rank = @N
);
END