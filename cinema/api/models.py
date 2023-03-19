from django.db import models

# Create your models here.

class Director(models.Model):
    full_name = models.CharField(max_length=255)
    birthday = models.DateTimeField()

    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'

    def __str__(self):
        return self.full_name

class Genre(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.title

class Film(models.Model):
    title = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.PROTECT)
    country = models.CharField(max_length=255)
    year_of_release = models.DateTimeField()
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

    def __str__(self):
        return self.title

class Poster(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    film = models.ForeignKey(Film, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Poster'
        verbose_name_plural = 'Posters'

    def __str__(self):
        return self.title