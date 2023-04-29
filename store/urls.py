
from django.contrib import admin
from django.urls import path, include

from store.views import IndexView

app_name = 'store'

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
]
