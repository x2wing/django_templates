from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),# при обращении к адресу ''(главная страница), будем использовать представление (термин Django) log
]