from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name_plural = "Genres"
    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    founded_year = models.PositiveIntegerField(null=True, blank=True)
    def __str__(self):
        return self.name


class AnimeSeries(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='series')
    studios = models.ManyToManyField(Studio, related_name='series')
    release_year = models.PositiveIntegerField()
    episodes = models.PositiveIntegerField()
    rating = models.FloatField(default=0.0)
    synopsis = models.TextField(blank=True, null=True)
    cover_image = models.CharField(max_length=200, blank=True, null=True, default='')
    def __str__(self):
        return self.title
