from django.shortcuts import render, get_object_or_404

from .models import Anime, Genre, Studio


# Inicio: una serie mejor valorada por género
def home(request):
    generos = Genre.objects.order_by('name')
    destacados = []

    for genero in generos:
        serie = genero.series.order_by('-rating', 'title').first()

        if serie is not None:
            destacados.append(serie)

    return render(
        request,
        'appAnime/home.html',
        {'destacados': destacados}
    )


# Listado de todas las series
def lista_series(request):
    series = (
        Anime.objects
        .select_related('genre')
        .prefetch_related('studios')
        .order_by('title')
    )

    return render(
        request,
        'appAnime/lista_series.html',
        {'series': series}
    )


# Detalle de una serie
def detalle_serie(request, anime_id):
    serie = get_object_or_404(
        Anime.objects
        .select_related('genre')
        .prefetch_related('studios'),
        pk=anime_id
    )

    return render(
        request,
        'appAnime/detalle_serie.html',
        {'serie': serie}
    )


# Listado de géneros
def lista_generos(request):
    generos = Genre.objects.order_by('name')

    return render(
        request,
        'appAnime/lista_generos.html',
        {'generos': generos}
    )


# Detalle de un género
def detalle_genero(request, genre_id):
    genero = get_object_or_404(Genre, pk=genre_id)

    return render(
        request,
        'appAnime/detalle_genero.html',
        {'genero': genero}
    )


# Listado de estudios
def lista_estudios(request):
    estudios = Studio.objects.order_by('name')

    return render(
        request,
        'appAnime/lista_estudios.html',
        {'estudios': estudios}
    )


# Detalle de un estudio
def detalle_estudio(request, studio_id):
    estudio = get_object_or_404(Studio, pk=studio_id)

    return render(
        request,
        'appAnime/detalle_estudio.html',
        {'estudio': estudio}
    )