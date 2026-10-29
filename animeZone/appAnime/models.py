from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Anime(models.Model):
    title = models.CharField(max_length=150)
    synopsis = models.TextField()
    release_year = models.PositiveIntegerField()
    rating = models.FloatField(default=0)

    # Una serie tiene un género principal.
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name='series'
    )

    # Una serie puede tener varios estudios.
    studios = models.ManyToManyField(
        Studio,
        related_name='series'
    )

    # La imagen es opcional; almacenamos su URL.
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.title