from django import forms
from .models import Anime


from django import forms
from .models import Anime

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = [
            'title',
            'synopsis',
            'release_year',
            'rating',
            'genre',
            'studios',
            'image_url',
        ]
        labels = {
            'title': 'Título',
            'synopsis': 'Sinopsis',
            'release_year': 'Año de estreno',
            'rating': 'Valoración',
            'genre': 'Género',
            'studios': 'Estudios',
            'image_url': 'URL de la imagen',
        }
        widgets = {
    'synopsis': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
}