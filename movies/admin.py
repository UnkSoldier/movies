from .models import Movie
from django.contrib import admin


#on envoie le modèle sur le site admin.
admin.site.register(Movie)