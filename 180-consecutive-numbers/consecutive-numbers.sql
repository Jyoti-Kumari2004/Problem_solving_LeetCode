# Write your MySQL query statement below
select distinct num as ConsecutiveNums from (select num,
lag(num,1,0) over() as prev1,
lag(num,2,0) over() as prev2
from Logs) as x
where x.num=x.prev1 and x.num=x.prev2