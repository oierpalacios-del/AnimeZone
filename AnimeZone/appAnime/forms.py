from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Anime
from datetime import date


class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = [
            'title', 'synopsis', 'release_year',
            'rating', 'genre', 'studios', 'image_url',
        ]

        labels = {
            'title': _('Título'),
            'synopsis': _('Sinopsis'),
            'release_year': _('Año de estreno'),
            'rating': _('Valoración'),
            'genre': _('Género'),
            'studios': _('Estudios'),
            'image_url': _('URL de la imagen'),
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
                _("El año debe estar entre %(min)s y %(max)s."),
                code='invalid_year',
                params={'min': 1900, 'max': current_year},
            )
        return year

    def clean_rating(self):
        rating = self.cleaned_data['rating']

        if rating < 0 or rating > 10:
            raise forms.ValidationError(
                _("La valoración debe estar entre 0 y 10."),
                code='invalid_rating',
            )
        return rating