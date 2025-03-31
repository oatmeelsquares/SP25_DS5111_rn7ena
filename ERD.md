# ERD reasoning

## Purpose

This report will be presented to a hypothetical company looking for data to support their investment decisions. The purpose of this report will be to answer a few simple questions:

1. Do more expensive stocks or cheaper stocks grow more?
2. Which stocks appear on the gainers list most frequently?
3. What is the best time of day to trade stocks?
4. What is the best day of the week to trade stocks?

## Methods

The data was collected from Yahoo and the Wall Street Journal gainers pages:

- https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200
- https://www.wsj.com/market-data/stocks/us/movers

Data was normalized using a factory design pattern. Yahoo data needed to be stripped of plus signs and WSJ symbols needed to be extracted from longer company names. Both processors returned normalized data with four fields: symbol, price, price change, and percent change.

Data will be processed into intermediate tables so that data can be easily drawn.

## Data Tables

The intermediate tables include:

- RAW
    - timestamp (primary key)
    - symbol (primary key)
    - price
    - change
    - percent change
- SYMBOL_STATS
    - symbol (primary key)
    - COUNT(\*) as count
    - AVG(price_change) as avg_price_change
    - AVG(price_percent_change) as avg_percent_change
- TIME_STATS
    - timestamp (primary key)
    - COUNT(\*) as count
    - AVG(price_change) as avg_change
    - AVG(price_percent_change) as avg_percent_change

The RAW table will remove duplicates and the source under the assumption that if both sources have overlapping symbols, the reported numbers will be the same. This removes the possiblity of slight discrepencies based on the few-second time between scraping the two different sources.

The final tables are:

- CHANGE_RATIO_SCATTER (derived from RAW)
    - price (x)
    - price_percent_change (y)
- TOP_FREQ_GAINERS_HIST (derived from SYMBOL_STATS)
    - symbol
    - count
- BEST_TIME_BAR (derived from TIME_STATS)
    - timestamp (grouped by time of day)
    - AVG(avg_percent_change) as avg_percent_change
- BEST_DAY_BAR (derived from TIME_STATS)
    - timestamp (grouped by day of the week)
    - AVG(avg_percent_change) as avg_percent_change

The final tables will map directly into plots, which are described in the table titles. Each of the final tables will produce a plot that gives direct insights into one of the four proposed questions. They describe the data in a visual way so as to gain useful insights from the raw data.
