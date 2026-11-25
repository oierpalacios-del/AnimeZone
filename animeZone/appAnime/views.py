from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Anime, Genre, Studio
from .forms import AnimeForm


# 1. Inicio: una serie mejor valorada por género (Sustituye a home)
class HomeView(TemplateView):
    template_name = 'appAnime/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        generos = Genre.objects.order_by('name')
        destacados = []

        for genero in generos:
            serie = genero.series.order_by('-rating', 'title').first()
            if serie is not None:
                destacados.append(serie)

        context['destacados'] = destacados
        return context


# 2. Listado de todas las series (Sustituye a lista_series)
class AnimeListView(ListView):
    model = Anime
    template_name = 'appAnime/lista_series.html'
    context_object_name = 'series'
    queryset = (
        Anime.objects
        .select_related('genre')
        .prefetch_related('studios')
        .order_by('title')
    )


# 3. Detalle de una serie (Sustituye a detalle_serie)
class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'appAnime/detalle_serie.html'
    context_object_name = 'serie'
    pk_url_kwarg = 'anime_id'
    queryset = (
        Anime.objects
        .select_related('genre')
        .prefetch_related('studios')
    )


# 4. Listado de géneros (Sustituye a lista_generos)
class GenreListView(ListView):
    model = Genre
    template_name = 'appAnime/lista_generos.html'
    context_object_name = 'generos'
    queryset = Genre.objects.order_by('name')


# 5. Detalle de un género (Sustituye a detalle_genero)
class GenreDetailView(DetailView):
    model = Genre
    template_name = 'appAnime/detalle_genero.html'
    context_object_name = 'genero'
    pk_url_kwarg = 'genre_id'


# 6. Listado de estudios (Sustituye a lista_estudios)
class StudioListView(ListView):
    model = Studio
    template_name = 'appAnime/lista_estudios.html'
    context_object_name = 'estudios'
    queryset = Studio.objects.order_by('name')


# 7. Detalle de un estudio (Sustituye a detalle_estudio)
class StudioDetailView(DetailView):
    model = Studio
    template_name = 'appAnime/detalle_estudio.html'
    context_object_name = 'estudio'
    pk_url_kwarg = 'studio_id'

# 8. Formulario para añadir nuevos animes
class AnimeCreateView(CreateView):
    model = Anime
    form_class = AnimeForm
    template_name = 'appAnime/anime_form.html'
    success_url = reverse_lazy('appAnime:lista_series')
