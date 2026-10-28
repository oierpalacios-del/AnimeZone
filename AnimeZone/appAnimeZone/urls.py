# appAnimeZone/urls.py
from django.urls import path
from . import views

app_name = 'appAnimeZone'

urlpatterns = [
    path('', views.home, name='index'),
    path('series/', views.series_list, name='series_list'),
    path('series/<int:pk>/', views.series_detail, name='series_detail'),
    path('generos/', views.generos_list, name='generos_list'),
    path('generos/<int:pk>/', views.generos_detail, name='generos_detail'),
    path('estudios/', views.estudios_list, name='estudios_list'),
    path('estudios/<int:pk>/', views.estudios_detail, name='estudios_detail'),
]