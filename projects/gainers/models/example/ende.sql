{{ config(materialized='table') }}

SELECT EN, DE
FROM DATA_SCIENCE.RN7ENA_RAW.NUMBERS
