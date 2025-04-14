{{ config(materialized='table') }}

SELECT FR
FROM DATA_SCIENCE.RN7ENA_RAW.NUMBERS
