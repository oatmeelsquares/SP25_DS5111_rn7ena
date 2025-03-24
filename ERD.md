# ERD reasoning

## Purpose

This report will be presented to a hypothetical company looking for data to support their investment decisions. The purpose of this report will be to answer a few simple questions:

1. Which stocks are on the gainers list the most?
2. Which stocks had the most growth?
3. Which stocks ended up with the highest positive change between the beginning and end?
4. Which stocks had the best ratio between growth and net positive change (measure of volitility)?

## Methods

The data was collected from Yahoo and the Wall Street Journal gainers pages:

- https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200
- https://www.wsj.com/market-data/stocks/us/movers

Data was normalized using a factory design pattern. Yahoo data needed to be stripped of plus signs and WSJ symbols needed to be extracted from longer company names. Both processors returned normalized data with four fields: symbol, price, price change, and percent change.

Data will be processed into INTERMEDIATE TABLES for SOME PURPOSE.

The final tables will be SOME FORMAT. This answers MY QUESTIONS because of SOME REASON. This describes what is in the gainers and how we would use them.
