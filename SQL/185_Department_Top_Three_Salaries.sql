select
    department,
    employee,
    salary
from (
    select
        d.name as Department,
        e.name as Employee,
        salary,
        dense_rank() over(partition by DepartmentId order by salary desc) rank
    from Employee e
    join Department d on d.id = e.DepartmentId
) t
where rank <= 3
order by salary desc;
