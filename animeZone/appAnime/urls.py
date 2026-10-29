from django.urls import path
from . import views

app_name = 'appAnime'

urlpatterns = [
    path('', views.home, name='home'),

    path(
        'series/',
        views.lista_series,
        name='lista_series'
    ),
    path(
        'series/<int:anime_id>/',
        views.detalle_serie,
        name='detalle_serie'
    ),

    path(
        'generos/',
        views.lista_generos,
        name='lista_generos'
    ),
    path(
        'generos/<int:genre_id>/',
        views.detalle_genero,
        name='detalle_genero'
    ),

    path(
        'estudios/',
        views.lista_estudios,
        name='lista_estudios'
    ),
    path(
        'estudios/<int:studio_id>/',
        views.detalle_estudio,
        name='detalle_estudio'
    ),
]