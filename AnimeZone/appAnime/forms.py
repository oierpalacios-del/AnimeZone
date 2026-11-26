from django import forms
from .models import Anime
from datetime import date

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
            'release_year': forms.TextInput(),
            'rating': forms.TextInput(),
        }

    def clean_release_year(self):
        year = self.cleaned_data['release_year']
        current_year = date.today().year

        if year < 1900 or year > current_year:
            raise forms.ValidationError(
                f"El año debe estar entre 1900 y {current_year}."
        )

        return year

    def clean_rating(self):
        rating = self.cleaned_data['rating']

        if rating < 0 or rating > 10:
            raise forms.ValidationError(
                "La valoración debe estar entre 0 y 10."
            )

        return rating