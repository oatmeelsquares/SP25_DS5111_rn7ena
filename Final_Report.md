


















# Exploring Stock Data with Snowflake

## Purpose

This report will be presented to a hypothetical company looking for data to support their investment decisions. The purpose of this report will be to answer a few simple questions:

1. Do more expensive stocks or cheaper stocks grow more?
2. Which stocks appear on the gainers list most frequently?
3. What is the best time of day to trade stocks?

## Methods

The data was collected from Yahoo and the Wall Street Journal gainers pages:

- https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200
- https://www.wsj.com/market-data/stocks/us/movers

Data was normalized using a factory design pattern. Yahoo data needed to be stripped of plus signs and WSJ symbols needed to be extracted from longer company names. Both processors returned normalized data with four fields: symbol, price, price_change, and price_percent_change.

Data was be processed into intermediate tables -- one aggregated by symbol, the other by time of day -- so that the final tables can be easily drawn.

The GAINERS table includes the raw data without duplicates under the assumption that if there are two lines that are exactly the same, they probably came from the two different sources and represent the same information. Data cleaning was limited, however, and duplicates may still exist due to tiny fluctuations in the seconds between collection by one source and another. This may skew the data, especially the count plots. However, since the purpose of this exercise is mainly to practice using snowflake and not to ensure total data integrity, the report assumes no friction.

The final tables map directly into the plots pictured below. Each of the final tables produces a plot that gives direct insights into one of the three proposed questions. They describe the data in a visual way so as to gain useful insights from the raw data. The visualizations were produced directly from the final tables in Snowflake.

## Results

### Relationship Between Stock Price and Growth

![](https://github.com/oatmeelsquares/SP25_DS5111_rn7ena/blob/main/figures/change_ratio_scatter.png)

This scatterplot shows the growth of each stock against its price. Based on the scatterplot, there does not seem to be any strong correlation between the raw price of a stock and its performance in the market.


### High-Frequency Gainers

![](https://github.com/oatmeelsquares/SP25_DS5111_rn7ena/blob/main/figures/top_freq_bar.png)

This horizontal bar chart shows the top 10 gainers by frequency. These stocks may offer more growth than others, however it is important to note that this chart does not account the *magnitude* of growth, so gains could be very small and offset by days of loss.


### Percent Change Throughout the Day

![](https://github.com/oatmeelsquares/SP25_DS5111_rn7ena/blob/main/figures/best_time_bar.png)

This bar chart shows how much growth is recorded at each time of day. All growth is measured from the start of the day, so the difference between bars is what's important to look at, not the raw values themselves. With that in mind, it looks like the biggest gains happen at market open and they peter out during the day.

## Conclusion

Stock trading is gambling! Do it for fun, but if you want your money to grow reliably, buy ETFs and make sure your portfolio is diversified.
