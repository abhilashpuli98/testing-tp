-- Last Updated: 2/5/2026, 9:22:33 AM
# Write your MySQL query statement below
select player_id,MIN(event_date) as first_login from Activity group by player_id;
