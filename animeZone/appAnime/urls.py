from django.urls import path
from .views import (
    HomeView,
    AnimeListView,
    AnimeDetailView,
    GenreListView,
    GenreDetailView,
    StudioListView,
    StudioDetailView,
    AnimeCreateView,
)

app_name = 'appAnime'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path(
        'series/',
        AnimeListView.as_view(),
        name='lista_series'
    ),
    path(
        'series/<int:anime_id>/',
        AnimeDetailView.as_view(),
        name='detalle_serie'
    ),

    path(
        'generos/',
        GenreListView.as_view(),
        name='lista_generos'
    ),
    path(
        'generos/<int:genre_id>/',
        GenreDetailView.as_view(),
        name='detalle_genero'
    ),

    path(
        'estudios/',
        StudioListView.as_view(),
        name='lista_estudios'
    ),
    path(
        'estudios/<int:studio_id>/',
        StudioDetailView.as_view(),
        name='detalle_estudio'
    ),
    path('series/nuevo/', AnimeCreateView.as_view(), name='crear_anime'),
    
]