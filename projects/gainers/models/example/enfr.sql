{{ config(materialized='table') }}

SELECT EN, FR
FROM DATA_SCIENCE.RN7ENA_RAW.NUMBERS
