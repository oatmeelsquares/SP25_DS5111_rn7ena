# ERD reasoning

## Purpose

This report will be presented to a hypothetical company looking for data to support their investment decisions. The purpose of this report will be to answer a few simple questions:

1. Do more expensive stocks or cheaper stocks grow more?
2. Which stocks appear on the gainers list most frequently?
3. What is the best time of day to trade stocks?

## Methods

The data was collected from Yahoo and the Wall Street Journal gainers pages:

- https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200
- https://www.wsj.com/market-data/stocks/us/movers

Data was normalized using a factory design pattern. Yahoo data needed to be stripped of plus signs and WSJ symbols needed to be extracted from longer company names. Both processors returned normalized data with four fields: symbol, price, price change, and percent change.

Data will be processed into intermediate tables -- one aggregated by symbol, the other by time of day -- so that data can be easily drawn.

The GAINERS table will include the raw data without duplicates under the assumption that if there are two lines that are exactly the same, they probably came from the two different sources and represent the same information. Data cleaning was limited, however, and duplicates may still exist due to tiny fluctuations in the seconds between collection by one source and another. This may skew the data, especially the count plots. However, since the purpose of this exercise is mainly to practice using snowflake and not to ensure total data integrity, the plan assumes no friction.

The final tables will map directly into plots, which are described in the table titles. Each of the final tables will produce a plot that gives direct insights into one of the three proposed questions. They describe the data in a visual way so as to gain useful insights from the raw data.

## Data Tables

![](https://github.com/oatmeelsquares/SP25_DS5111_rn7ena/blob/main/figures/ERD.png)


This ER diagram was rendered using [mermaidjs.live](https://mermaid.live/edit#pako:eNqtUcFOwzAM_RXL4gBSKrWIsa0HTly5sBsLB6_x2ow2qdJkWjXt30mbji8gh5f37Bc7sq9YWcVYojQQz2WsGnI-O7CnFPHatwwSd9TyAJ98ZhNY3u0ZXfQA-xMZAUc-COjICaDeTWwUcApmgjbGQi1g4F6ArbwAY88CFFffqdCYCklcGsCjNvDwJBFe8jyHLHuDoogsuQ_kYL-KUsDrjOvVhJvnCbczL_J0FXlSKTXjZs6s_54vX2i14f-sigI7dh1pFad7nXpI9A13cXhlpIrczzTGW_RR8HY3mgpL7wILDL0iz--aakfdPchKe-s-0rbmpQl0NtQNlkdqh-joyXxZ2y369gs444Ie) with the code found in [scripts/ERD.mermaidjs](https://github.com/oatmeelsquares/SP25_DS5111_rn7ena/blob/main/scripts/ERD.mermaidjs).

The intermediate tables include:

- GAINERS
    - timestamp
    - symbol
    - price
    - change
    - percent_change
    - date
    - time (morning, midday, or evening)
- SYMBOL_STATS (grouped by symbol)
    - symbol
    - COUNT(\*) as count
    - AVG(price_change) as avg_change
    - AVG(price_percent_change) as avg_percent_change
- TIME_STATS (grouped by time)
    - time
    - COUNT(\*) as count
    - AVG(price_change) as avg_price
    - AVG(price_percent_change) as avg_percent_change

The final tables are:

- CHANGE_RATIO_SCATTER (derived from GAINERS)
    - price (x)
    - price_percent_change (y)
- TOP_FREQ_HIST (derived from SYMBOL_STATS)
    - symbol (x)
    - count (y)
- BEST_TIME_BAR (derived from TIME_STATS)
    - time
    - avg_percent_change
