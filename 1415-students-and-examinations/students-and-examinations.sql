# Write your MySQL query statement below
select s.student_id,s.student_name,sb.subject_name,
count(e.subject_name) as attended_exams
from Students as s
cross join Subjects as sb
left join Examinations as e
on e.student_id=s.student_id and
sb.subject_name=e.subject_name
group by s.student_id,s.student_name,sb.subject_name
order by s.student_id
