from django.contrib import admin
from .models import Genre, Studio, Anime


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_year', 'rating')
    list_filter = ('genre', 'release_year')
    search_fields = ('title',)
    filter_horizontal = ('studios',)
