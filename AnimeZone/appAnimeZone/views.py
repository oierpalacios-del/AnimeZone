from django.http import HttpResponse
from .models import AnimeSeries, Genre, Studio


#devuelve la portada (una serie destacada por género)
def home(request):
    generos = Genre.objects.all()
    output = ""
    for genero in generos:
        serie = genero.series.order_by('-rating').first()
        if serie:
            output += f"Género: {genero.name} - Mejor Serie: {serie.title} ({serie.rating})\n"
    return HttpResponse(output)

#devuelve el listado de series
def series_list(request):
    series = AnimeSeries.objects.order_by('title')
    output = ', '.join([s.title for s in series])
    return HttpResponse(output)

#devuelve los datos de una serie
def series_detail(request, serie_id):
    serie = AnimeSeries.objects.get(pk=serie_id)
    estudios = ', '.join([s.name for s in serie.studios.all()])
    output = f'Detalles de la serie: {serie.id}, {serie.title}. Género: {serie.genre.name}. Año: {serie.release_year}. Rating: {serie.rating}. Estudios: {estudios}'
    return HttpResponse(output)

#devuelve el listado de géneros
def generos_list(request):
    generos = Genre.objects.order_by('name')
    output = ', '.join([g.name for g in generos])
    return HttpResponse(output)

#devuelve los detalles de un género
def generos_detail(request, genero_id):
    genero = Genre.objects.get(pk=genero_id)
    series = ', '.join([s.title for s in genero.series.all()])
    output = f'Detalles del género: {genero.id}, {genero.name}. Series: {series}'
    return HttpResponse(output)

#devuelve el listado de estudios
def estudios_list(request):
    estudios = Studio.objects.order_by('name')
    output = ', '.join([s.name for s in estudios])
    return HttpResponse(output)

#devuelve los detalles de un estudio
def estudios_detail(request, estudio_id):
    estudio = Studio.objects.get(pk=estudio_id)
    series = ', '.join([s.title for s in estudio.series.all()])
    output = f'Detalles del estudio: {estudio.id}, {estudio.name}. Series producidas: {series}'
    return HttpResponse(output)