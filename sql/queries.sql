create database insurance_analysis 

use insurance_analysis 

select * from policy_sales

select * from claims

SELECT COUNT(*)
FROM claims
WHERE Claim_Date IS NULL;

r SELECT Claim_Type, COUNT(*)
FROM claims
WHERE Claim_Date IS NULL
GROUP BY Claim_Type;

drop table claims

-- Q1:
select sum(premium) AS premium_2024 from policy_sales
where year(Policy_Purchase_Date) = 2024

-- Q2:
select year(Claim_date) as claim_year , 
month(Claim_date) as claim_month ,
sum(Claim_amount) as claim_amount
from claims
where year(Claim_date) in (2025,2026)
group by year(Claim_date) , month(Claim_date)
order by year(Claim_date) , month(Claim_date)


-- Q3:
select p.Policy_Tenure,
sum(c.Claim_Amount) as total_claims,
sum(p.Premium) as total_premium,
sum(c.Claim_Amount) * 1.0/ sum(p.Premium) as claim_cost_premium_ratio
from policy_sales p
LEFT JOIN claims c
on p.Vehicle_ID = c.Vehicle_ID
group by p.Policy_Tenure
order by p.Policy_Tenure;


--Q4:
select datename(month, p.Policy_Purchase_Date) as sale_month,
sum(c.Claim_Amount)* 1.0 / sum(p.Premium) as claim_ratio
from policy_sales p
left join claims c
on p.Vehicle_ID = c.Vehicle_ID
group by datename(month, p.Policy_Purchase_Date),month(p.Policy_Purchase_Date)
order by month(p.Policy_Purchase_Date);


--Q5:
select count(*) as vehicles_without_claim,
cast(count(*) as bigint) * 10000 as potential_claim_liability
from policy_sales p
left join claims c
on p.Vehicle_ID = c.Vehicle_ID
where c.Vehicle_ID is null;


-- Q1&3 Bonus:
select p.Policy_Tenure, sum(c.Claim_Amount) as total_claims, sum(p.Premium) as total_premium, sum(c.Claim_Amount) * 1.0 / sum(p.Premium) as loss_ratio
from policy_sales p
left join claims c
on p.Vehicle_ID = c.Vehicle_ID
group by p.Policy_Tenure
order by p.Policy_Tenure;

-- Q6:
select 
    sum(
        (Premium * 1.0 / datediff(day, Policy_Start_Date, Policy_End_Date)) *
        datediff(day, Policy_Start_Date, '2026-02-28')
    ) as earned_premium_till_feb_2026
from policy_sales
where Policy_Start_Date <= '2026-02-28';

-- Q6:
select 
    (sum(Premium) - (
        select 
            sum(
                (p.Premium * 1.0 / datediff(day, p.Policy_Start_Date, p.Policy_End_Date)) *
                case 
                    when '2026-02-28' > p.Policy_End_Date 
                        then datediff(day, p.Policy_Start_Date, p.Policy_End_Date)
                    else datediff(day, p.Policy_Start_Date, '2026-02-28')
                end
            )
        from policy_sales p
        where p.Policy_Start_Date <= '2026-02-28'
    )) / 46.0 as expected_monthly_premium
from policy_sales;




























