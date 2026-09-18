# Write your MySQL query statement below
with ranked as (
select e.*,
dense_rank() over(partition by departmentId order by Salary desc ) as rnk
from Employee as e)
select d.name as Department,rn.name as Employee,rn.salary as Salary
from ranked as rn
join department as d
on rn.departmentId=d.id
where rn.rnk<=3
