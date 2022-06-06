# StockMarket-analysis-using-MACD

In this project I've developed the Stock Market Trading System using MACD (Moving Average Convergence Divergence).

Now before understanding the MACD stratergy let's first understand what is Moving Averages?

Moving Averages are nothing but a technical analysis tool whcih is commonly used as a stock market indicator. Moving Average can be of 10 min, 1day, 1 week, or even years.
Using Moving Averages one can get idea about buying and selling opportunities in the Stock Market. Generally to calculate Moving Average of a stock for some defined period
of time we will take the average of the stock price for the specified duration of the time! Yes, it is as simple as it sounds!! 

Now, the next question is how can we use it to analyze the stock? Well, it is also a very simple statistical analysis. When the stock price trades above its average price, it means the traders are willing to buy the stock at a price higher than its average price. This means the traders are optimistic about the stock price going higher. Therefore one should look at buying opportunities. And when the stock price trades below its average price, it means the traders are willing to sell the stock at a price lesser than its average price. This means the traders are pessimistic about the stock price movement. Therefore one should look at selling opportunities. 

There are several types of moving average which can be used. To understand about it more thoroughly please refer to https://zerodha.com/varsity/chapter/moving-averages/.

Now, after we have a good understanding of what is Moving Averages let's find out what is MACD and its application in stock analysis.

MACD is also a technical tool used for getting better understanding of the market tredns. There are major 3 components in MACD:
1. MACD line: Difference between 2 Exponential Moving Average lines.(Lesser M.A- greater M.A). Don't worry! It is not as complicated as it seems in the first look. Let's try to understand it using simple logic. The first moving average is for smaller period of time, so it obious that it is more influenced by the recent prices of the stock than the second moving average. Now when the smaller moving average crosses above the longer moving average we can infer that there must be a good amount of investment happened in the recent times, and if this trend lasts for a long duration we can say that there is a good chance of this trend to be backed up by the industrial traders. So it is a good opportunity to buy the stocks and vice versa. 
But, Traders generally argue that while waiting for the MACD line to crossover the centerline, a bulk of the movie would already be done and perhaps it would be late to enter a trade. To overcome this, there is an improvisation over this basic MACD line. The improvisation comes in the form of an additional MACD component which is the 9-day signal line. A 9-day signal line is an exponential moving average (EMA) of the MACD line.

2. Signal line: 9 day EWM of MACD line
3. HIST = MACD line - Signal Line

To some up the stratergy in a line:
IF MACD LINE > SIGNAL LINE => BUY THE STOCK 
IF SIGNAL LINE > MACD LINE => SELL THE STOCK

You can find more information about this on https://zerodha.com/varsity/chapter/indicators-part-2/

Anyone who knows the stock market knows that no technique is perfect and the market always manages to surprise us as there are many factors affecting the stock prices. MACD stratergy usually generates good results when the market is in uptrend. But it might not work when the market is facing the downtrend or sideways trend. To overcome this I have include the 200 day moving average in my code. 200 day span is very long period of time. So if the pricing line is above the 200 day moving average it means market should be facing uptrend and vice versa. So, using this knowledge we will only apply the MACD stratergy to buy and sell the stock when the market is in uptrend.

Now, about this project, I have created a simulation of Automated Trade for the duration of 30 days starting from the given date. According to the MACD stratergy, the recommendation to buy,sell or hold the stock will be generated for the particular date. You just have to enter the buying or selling qty and the account number generated. 
I've tried to keep my code as simple as possible. Hope you will easily understand everything from it.

@shyamal
