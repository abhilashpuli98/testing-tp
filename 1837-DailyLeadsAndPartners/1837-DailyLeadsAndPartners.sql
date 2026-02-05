-- Last Updated: 2/5/2026, 9:21:56 AM
# Write your MySQL query statement below
select date_id,make_name,count(DISTINCT lead_id) as unique_leads, count(distinct partner_id) as unique_partners
from DailySales
group by date_id,make_name;