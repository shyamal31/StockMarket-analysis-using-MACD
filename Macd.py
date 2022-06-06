import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import time
from fetch_data import stock_data
from Trading_account import Account

class ComponentsMACD:

    #Create datascice from the original Dataframe
    def select_dataslice(self,dataframe):
        self.dataframe = dataframe
        start = input('Start Date: ')
        end = input("End Date: ")
        self.new_df = self.dataframe[start:end]
        return self.new_df

    #Difference of 12 and 26 Day Moving Average
    def macd(self,small_offset=12, long_offset=26):
        EWM1 = self.new_df.Close.ewm(span = small_offset, adjust = False).mean()
        EWM2 = self.new_df.Close.ewm(span = long_offset, adjust =False).mean()
        self.macd_points = EWM1 - EWM2
        return self.macd_points

    #9 Day Moving Average of MACD points
    def signal(self, span=9):
        self.signal_line = self.macd_points.ewm(span = span, adjust =False).mean()

        return self.signal_line

    #Difference between MACD and Signal lines
    def hist(self):
        self.hist = self.macd_points - self.signal_line

        return self.hist

    #200 Day Moving Average to Check the tred of the market
    def twoHundredDayEMA(self):
        th_ema = pd.DataFrame(self.new_df.Close.ewm(span = 200, adjust =False).mean())
        th_ema = th_ema.rename(columns = {'Close':'200EMA'})
        return th_ema

    #combining macd,signal and hist into a dataframe
    def components(self):
        
        macd_df = pd.DataFrame(self.macd_points)
        macd_df.rename(columns= {'Close':'macd'}, inplace = True)

        signal_df = pd.DataFrame(self.signal_line)
        signal_df.rename(columns = {'Close':'signal'}, inplace =True)
        hist_df = pd.DataFrame(self.hist)
        hist_df.rename(columns = {'Close': 'hist'}, inplace = True)

        self.components = pd.concat([macd_df, signal_df, hist_df], join = 'inner', axis =1)
        return self.components   
    
    #combining all the elements into a dataframe
    def all_components(self):
        th_df = self.twoHundredDayEMA()
        closing_price = self.new_df.Close
        ac = pd.concat([self.components,th_df,closing_price], join ='inner',axis = 1)
        return ac


class Plot_graphs:
    #Line plot
    def line_plot(self,dataframe,column_name):
        line = go.Scatter(
            x = dataframe.index,
            y = dataframe[column_name],
            mode = 'lines',
            name = column_name
        )
        return line
    
    #Plot the candle chart 
    def candle_graph(self,dataframe_slice):
        candle = go.Candlestick(
            x = dataframe_slice.index,
            low = dataframe_slice.Low,
            high = dataframe_slice.High,
            close = dataframe_slice.Close,
            open = dataframe_slice.Open,
            increasing_line_color  = 'green',
            decreasing_line_color = 'red',
            name = 'Closing Price'

        )
        return candle

    #Creating MACD line object 
    def macdGraph(self,dataframe_components):

        macd_line= go.Scatter(
            x = dataframe_components.index,
            y = dataframe_components.macd,
            mode = 'lines',
            name = 'MACD line'
        )
        return macd_line   

    #Creating the Signal line object
    def signalGraph(self,dataframe_components):

        signal_line =  go.Scatter(
            x = dataframe_components.index,
            y = dataframe_components.signal,
            mode = 'lines',
            name = 'SIGNAL line'
        )
        return signal_line

    #Creating the Histogram object
    def histogram(self,dataframe_components):
        
        hist_plot = go.Bar(
            x = dataframe_components.index,
            y = dataframe_components['hist']
        )
        return hist_plot

    #Plot elements in a single graph
    def plot_graph(self,add_graphs):

        fig = go.Figure()
        for i in add_graphs:
            fig.add_trace(i)

        fig.update_layout(height = 600, width = 600,template = 'plotly_dark', yaxis_title = 'PRICE (USD)',xaxis_title = 'Dates', dragmode = False, modebar_remove = 'zoom2d')
        fig.show(config = {'displayModeBar': False})

    #Plot subplots
    def plot_subplots(self,add_graphs, rows, cols, row_heights, graph_in_row1 = []):

        fig = make_subplots(vertical_spacing = 0, rows=rows, cols=cols, row_heights=row_heights)

        if len(graph_in_row1) > 0:
            for i in graph_in_row1:
                fig.add_trace(i, row=1,col=1)
        for i in add_graphs:
            fig.add_trace(i, row=rows, col=1)

        fig.update_layout(height = 600, width = 800,template = 'plotly_dark', yaxis_title = 'PRICE (USD)',xaxis_title = 'Dates', dragmode = False, modebar_remove = 'zoom2d')
        fig.show(config = {'displayModeBar': False})


class Trade:
    buy_list = []
    sell_list =[]
    buy_signals = [0]
    sell_signals = [0]
    number_of_stocks = 0


    def portfolio(self):
        return self.number_of_stocks

    def recommend_buy_sell(self,date, all_components):
        # date = input("Enter the date (yyyy-mm-dd): ")
        row = all_components.loc[date]
        print(f'Current_value: ${row.Close}')
        if (row.macd > row.signal) and (row.Close > row['200EMA']):
            if self.buy_signals[-1] == 0:                        #0==> buy and 1==>hold
                self.buy_list.append(row.Close)
                self.buy_signals.append(1)
                self.sell_signals.append(0)

                return "BUY"
            else: 
                return "HOLD"

        elif (row.macd<row.signal) and (row.Close > row['200EMA']):
            if self.sell_signals[-1] ==0:                       #0==> sell and 1==>hold
                if self.number_of_stocks>0:
                    self.sell_list.append(row.Close)
                    self.sell_signals.append(1)
                    self.buy_signals.append(0)

                    return "SELL"
                else:
                    return f"You have {self.number_of_stocks} in your portfolio"
            else:
                return 'Avoid buying or selling the stock right now'

        else:
            return 'avoid buying or selling the stock right now'

    def execute(self,buy_sell):
        if buy_sell == 'BUY':
            buy_qty = int(input("Enter the buy QTY: "))
            self.number_of_stocks+=buy_qty
            buy_price = self.buy_list[-1]
            a =Account()
            print(a.withdraw_money(buy_qty*buy_price))   
        
        elif buy_sell == 'SELL':
            sell_qty = int(input("Enter the sell QTY: "))
            self.number_of_stocks-=sell_qty
            sell_price = self.sell_list[-1]
            a =Account()
            print(a.transfer_money(sell_qty*sell_price)) 
        else:
            print(buy_sell)

    def automated_trade(self,time_period,all_components):                   #add the time_period for which you want to automate the trade
        current_date = input("Please Enter the date in yyyy/mm/dd format: ")
        curr_index = all_components.index.get_loc(current_date)

        for i in all_components.index[curr_index:curr_index+time_period]:
            print(f'Date: {i}')
            buy_sell = self.recommend_buy_sell(i,all_components)
            self.execute(buy_sell)
            time.sleep(2)  #You can change the time interval as per your need 


comp = ComponentsMACD()
new_dataframe = comp.select_dataslice(stock_data)
comp.macd()
comp.signal()
comp.hist()
comp.twoHundredDayEMA()
comp.components()
all_components = comp.all_components()

