from django.urls import path

from num.views import *

app_name = 'num'

urlpatterns = [
    path('one/',one,name='one'),
]