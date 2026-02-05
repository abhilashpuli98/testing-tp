-- Last Updated: 2/5/2026, 9:24:35 AM
# Write your MySQL query statement below
SELECT
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;