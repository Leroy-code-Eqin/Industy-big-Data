from django.contrib import admin
from django.urls import path
from . import views
app_name='Data'
urlpatterns = [
    path('', views.searchPage,name='index'),
    path('rept/',views.respond,name='respond')
]