-- Last Updated: 2/5/2026, 9:24:32 AM
# Write your MySQL query statement below
select name as Customers  from Customers where id not in(select customerId from Orders);
