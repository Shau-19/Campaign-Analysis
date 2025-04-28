CREATE DATABASE adidas_db;
USE adidas_db;
CREATE TABLE campaigns_data (
    Campaign_ID VARCHAR(20),
    Campaign_Name VARCHAR(255),
    Product_Category VARCHAR(100),
    Channel VARCHAR(100),
    Impressions INT,
    Clicks INT,
    Conversions INT,
    Cost FLOAT,               
    Revenue FLOAT,
    Promo_Type VARCHAR(100)
);
SELECT * FROM campaigns_data;
-- 1. Calculate CTR(CLick Through Rate) by Campaign
SELECT 
    Campaign_Name,
    ROUND((SUM(Clicks) / SUM(Impressions)) * 100, 2) AS CTR_Percentage,
    SUM(Conversions) AS Total_Conversions
FROM 
    campaigns_data
GROUP BY 
    Campaign_Name
ORDER BY 
    CTR_Percentage DESC
LIMIT 10;

-- 2. Compare Conversion Rates By Channel

Select 
	Channel,
    round((sum(Conversions)/sum(Clicks))*100,2) AS Conversion_Rate_Percentage,
    sum(Revenue) as Total_Revenue
From campaigns_data
group by Channel
Order By Conversion_Rate_Percentage DESC;

-- 3 Calculate ROI by Promotion type
select 
Promo_Type,
round(( (sum(Revenue) - sum(Cost))/sum(Cost))*100,2) as ROI_Percentage
FROM campaigns_data
group by Promo_Type
order by ROI_Percentage DESC;

-- 4. Top 5 Campaigns by Revenue

SELECT 
    Campaign_Name,
    SUM(Revenue) AS Total_Revenue,
    SUM(Cost) AS Total_Cost
FROM campaigns_data
GROUP BY Campaign_Name
ORDER BY Total_Revenue DESC
LIMIT 5;









