from django.shortcuts import render,redirect
import datetime as dt
from .models import tbStockList, tbMyStocks
#from .filters import symbolFilter
from django.db.models import Count

# Create your views here.

def home(request):

    today = dt.date.today()
    template_name = 'stockData/home.html'

    # stock_list = tbStockList.objects.all()
    # my_stocks = tbMyStocks.objects.all()


    my_stocks = list(tbMyStocks.objects.all())
    #print(my_stocks)
    stock_list = list(tbStockList.objects.exclude(Symbol__in=my_stocks[:]).exclude())
    count_stocks = tbStockList.objects.exclude(Symbol__in=my_stocks[:]).exclude().count()
    count_my_stocks = tbMyStocks.objects.all().count() #tbMyStocks.objects.all().count()
    max_stocks = 20
    count_left = max_stocks - count_my_stocks
    s1 = int(count_stocks/2)
    s2 = count_stocks
    #print(s1)
    args = {'Today':today, 'Stocks1':stock_list[0:s1], 'Stocks2':stock_list[(s1):(s2)], 'myStocks':my_stocks, 'countStock':count_stocks, 'mycount':count_my_stocks, 'count_left':count_left, 'max':max_stocks }

    return render(request, template_name, args)


def change_stockList(request, operation, symbol):

    mysymbol = symbol

    if operation == 'add':
        
        newsymbol = tbMyStocks()
        newsymbol.Symbol = symbol
        newsymbol.save()

    elif operation == 'remove':

        newsymbol = tbMyStocks()
        newsymbol.id = symbol
        newsymbol.delete()

    return redirect('stockData:home')


