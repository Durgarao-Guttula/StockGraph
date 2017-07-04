from django.conf.urls import url, include
#from . import views
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    #url(r'^symconn/(?P<operation>.+)/(?P<symbol>[a-zA-Z]([\w -]*[a-zA-Z]\.\w))/$', views.change_stockList, name='change_stockList')
    url(r'^symconn/(?P<operation>.+)/(?P<symbol>[a-zA-Z]([\w -]*[a-zA-Z]\.\w)|or|\d*)/$', views.change_stockList, name='change_stockList')

    #/home/homeX/
]