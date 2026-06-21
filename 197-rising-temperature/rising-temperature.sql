# Write your MySQL query statement below
-- select x.id from
-- (select w.*,
-- lag(temperature) over(order by w.recordDate asc) as prev_temp
-- from Weather as w) as x
-- where x.prev_temp is not null and x.temperature>x.prev_temp;

-- since this is not correct for the previous value we need to find diff approach

select w.id
from Weather as w
join Weather as w1
on Date_sub(w.recordDate,interval 1 day)=w1.recordDate
where w.temperature>w1.temperature;
