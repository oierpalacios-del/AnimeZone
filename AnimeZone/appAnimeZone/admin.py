from django.contrib import admin
from .models import Genre, Studio, AnimeSeries

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ('name', 'founded_year')
    search_fields = ('name',)

@admin.register(AnimeSeries)
class AnimeSeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_year', 'rating')
    list_filter = ('genre',)
    filter_horizontal = ('studios',)   # Widget visual para ManyToMany
