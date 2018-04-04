
from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'dataapp'

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^json/',views.list,name='json'),
   url(r'^json2/',views.ItemApi,name='item')
]