-- Last Updated: 2/5/2026, 9:24:33 AM
# Write your MySQL query statement below
select email from Person group by email having count(email)>1;