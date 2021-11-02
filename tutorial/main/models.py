from django.db import models


class Actor(models.Model):
    # movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return "{}".format(self.name)


class Movie(models.Model):
    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_R = 3
    RATINGS = (
        (NOT_RATED, "NR - Not Rated"),
        (RATED_G, "G - General Audiences"),
        (RATED_PG, "PG - Parental Guidance"),
        (RATED_R, "R - Restricted")
    )

    title = models.CharField(max_length=100)
    plot = models.TextField()
    year = models.PositiveIntegerField(blank=True)
    rating = models.IntegerField(choices=RATINGS, default=NOT_RATED)
    runtime = models.PositiveIntegerField(default=120)
    actors = models.ManyToManyField(Actor, blank=True)

    class Meta:
        ordering = ["-year", "title"]

    def __str__(self):
        return "{} ({})".format(self.title, self.year)
