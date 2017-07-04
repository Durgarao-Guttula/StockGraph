#from random import randint
from datetime import datetime, timedelta
from pandas import pandas as pd
from pandas_datareader import data, wb
#import pandas_datareader as pdr
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
#from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt 
import numpy as np
import bs4 as soup
from stockData.models import tbMyStocks

# Create your views here.

style.use('ggplot')
today = dt.date.today()
dtStart = (dt.datetime.strptime("2017-01-01", '%Y-%m-%d'))
dtEnd = (dt.datetime(today.year,today.month,today.day)).isoformat(' ') 

def genGraph(graph_filename):

    dtStart = (dt.datetime.strptime("2016-08-01", '%Y-%m-%d'))
    my_stocks = tbMyStocks.objects.all()
    main_df = pd.DataFrame()
    df = pd.DataFrame()

    print('Number of Stocks:',len(my_stocks))

    if len(my_stocks)==0:
        
        return False

    else:        
        
        for sym in my_stocks:
            if main_df.empty:

                main_df = (data.get_data_google(sym.Symbol, dtStart)['Close'])
                main_df = main_df.to_frame()
                main_df.rename(columns = {'Close' : sym.Symbol}, inplace=True)
                #print(main_df.head())
                
            else:
                main_df = main_df.join((data.get_data_google(sym.Symbol, dtStart)['Close']), how='outer')
                main_df.rename(columns = {'Close' : sym.Symbol}, inplace=True)
                #print(main_df)
        else:
            pass  
        fig = Figure()
        ax1 = fig.add_subplot(1,1,1)
        #ax2 = fig.add_subplot(1,1,1)
        #lines, labels = ax.legend_handles_labels()
        #plt.legend(my_stocks)
        ax1.plot(main_df.index, main_df)
        ax1.legend(main_df.columns[:], loc='upper left')
        #ax2.plot(main_df)

        canvas = FigureCanvas(fig)
        canvas.print_png(graph_filename)

        return True