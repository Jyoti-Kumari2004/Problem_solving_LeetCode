# Write your MySQL query statement below
select e.name
from employee as e
inner join employee as ee
on e.id=ee.managerId
group by e.id
having count(ee.id)>=5

