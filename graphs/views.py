from django.shortcuts import render,redirect
from . import graphs
from django.conf import settings as djangoSettings
import os.path
from stockData.models import tbMyStocks


def graph(request):

    from datetime import datetime, timedelta

    datetoday,datef = datetime.utcnow().strftime("%Y%m%d%M"), datetime.utcnow().strftime("%B %d %Y,%H:%M:%S")
    graph_filename = (djangoSettings.STATICFILES_DIRS[0] + 'graph_' + datetoday + '.png')
    filename = ('graph_' + datetoday + '.png')
    my_stocks = tbMyStocks.objects.all()

    template_name = 'stockData/select.html'

    if len(my_stocks)==0:
        
        args = {'Return':"Select a Stock!"}
            
        return render(request, template_name, args)

    else:
        
        if not os.path.exists(graph_filename):
            graphs.genGraph(graph_filename)
            args = {'Value':'Generated','DateF':datef,'Filename':filename}
            return render(request, 'graphs/home.html', args)
        else:
            args = {'Value':'FromCache','DateF':datef,'Filename':filename}        
            return render(request, 'graphs/home.html', args)

