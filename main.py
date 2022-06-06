import pandas as pd
from Macd import Trade,all_components,new_dataframe,Plot_graphs
from Trading_account import Account

if __name__ == "__main__":
    #Testing our Stratergy on paper money
    # my_account = Account()
    # acc1 = my_account.create_account()
    # # acc_number = acc1[0]

    # my_account.transfer_money(10**5)

    # trading = Trade()

    # trading.automated_trade(30,all_components)
    # # print(trading.buy_list)
    # # print(trading.sell_list)

    # print(trading.portfolio())

    #Plot Graphs
    plt = Plot_graphs()
    line = plt.line_plot(all_components,'200EMA')
    candleGraph = plt.candle_graph(new_dataframe)
    macd_plot = plt.macdGraph(all_components)
    signal_plot= plt.signalGraph(all_components)
    hist_plot= plt.histogram(all_components)

    graph = plt.plot_subplots(add_graphs =[macd_plot,signal_plot,hist_plot],rows =3, cols=1, row_heights=[20,10,20], graph_in_row1=[candleGraph,line])

