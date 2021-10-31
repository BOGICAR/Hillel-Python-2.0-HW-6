from django.contrib import admin
from .models import Movie, Actor


class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "rating")
    list_filter = ("rating",)
    fields = (
        (
            "title",
            "year"
        ),
        "runtime",
        "rating",
        "plot",
    )
    search_fields = ["title"]


class ActorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    search_fields = (
        "name",
    )

    def name(self, obj):
        return "{}".format(obj.name)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
