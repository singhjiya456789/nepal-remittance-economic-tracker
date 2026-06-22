-- Query 1: RANK
-- Question: Which years had the highest remittance inflow?
select yr, remittance_usd, pct_gdp ,
rank() over ( order by remittance_usd desc) as remittance_rank 
from remittance_by_year;

SELECT * FROM (
    SELECT yr, remittance_usd, pct_gdp,
        RANK() OVER (ORDER BY remittance_usd DESC) AS remittance_rank
    FROM remittance_by_year
) AS ranked
ORDER BY remittance_rank DESC
LIMIT 1;

-- Query 2: LAG
-- Question: How much did remittance inflow change compared to the previous year?
select yr, remittance_usd, pct_gdp, 
lag(remittance_usd) over (order by yr) as previous_yr_remittance,
remittance_usd - lag(remittance_usd) over (order by yr ) as yoy_change_usd
from remittance_by_year;

-- Query 3: Running Total
-- Question: What is the cumulative total remittance Nepal has received from 1993 up to each year?
SELECT yr, remittance_usd,
    SUM(remittance_usd) OVER (ORDER BY yr) AS cumulative_total
FROM remittance_by_year;

-- Query 4: CTE (Common Table Expression)
-- Question: Which years did remittance grow by more than 10% compared to the previous year?
with yoy_cte as (select yr, remittance_usd, pct_gdp, 
lag(remittance_usd) over (order by yr) as previous_yr_remittance,
remittance_usd - lag(remittance_usd) over (order by yr ) as yoy_change_usd from remittance_by_year)
select * from yoy_cte 
where yoy_change_usd > 0.10*previous_yr_remittance;