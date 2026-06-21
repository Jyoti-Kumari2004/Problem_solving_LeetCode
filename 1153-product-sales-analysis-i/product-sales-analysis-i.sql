# Write your MySQL query statement below
select p.product_name,s.year,s.price
from Product as p
natural join Sales as s;
