from django.urls import path

from alpha.views import *

app_name = 'alpha'

urlpatterns = [
    path('a/',a,name='a'),
]