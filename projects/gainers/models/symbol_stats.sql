{{ config(materialized='table') }}

SELECT
	SYMBOL,
	COUNT(*) AS COUNT, 
	AVG(PRICE_CHANGE) AS AVG_CHANGE,
	AVG(PRICE_PERCENT_CHANGE) AS AVG_PERCENT_CHANGE
FROM DATA_SCIENCE.RN7ENA.GAINERS
GROUP BY SYMBOL
ORDER BY SYMBOL
