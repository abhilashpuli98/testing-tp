-- Last Updated: 2/5/2026, 9:23:11 AM
# Write your MySQL query statement below
update salary
set sex =  case when sex="f" then "m"
when sex = "m" then "f"
end;