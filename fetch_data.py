import pandas_datareader.data as pdr
import pandas as pd
#COLLECT data from pandas_datareader and save it to local machine
class fetch:
    global stock_data
    def __init__(self,stock_symbol,stock_name):
        self.stock_symbol = stock_symbol
        self.stock_name = stock_name
        
    
    def get_stock_data(self):
        self.stock_data = pdr.get_data_yahoo(self.stock_symbol)
        return self.stock_data

    def save_csv(self,stock,path):
        stock.to_csv(path+f'\\{self.stock_name}.csv')



# stockname = 'TSLA'
# stock_data= get_stock_data(stockname)
# save_csv(stock_data,'C:\\Users\\Admin\\OneDrive - pdpu.ac.in\\Desktop\\SHYAMAL\\projects\\StockMarket', 'TeslaStock')

path = 'C:\\Users\\Admin\\OneDrive - pdpu.ac.in\\Desktop\\SHYAMAL\\projects\\StockMarket'
company = fetch("TSLA",'TeslaStock')
stock_data = company.get_stock_data()
company.save_csv(stock_data,path) #Enter the path where you want to save the csv file
