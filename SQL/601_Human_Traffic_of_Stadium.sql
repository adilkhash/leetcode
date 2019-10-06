select id,
       visit_date,
       people
from (
         select id,
                visit_date,
                people,
                lag(people) over (order by id)     as prev_p1,
                lag(people, 2) over (order by id)  as prev_p2,
                lead(people, 1) over (order by id) as next_p1,
                lead(people, 2) over (order by id) as next_p2
         from stadium
     ) as t
where (prev_p1 >= 100 and prev_p2 >= 100 and people >= 100)
   or (people >= 100 and next_p1 >= 100 and next_p2 >= 100)
   or (people >= 100 and next_p1 >= 100 and prev_p1 >= 100)
order by id