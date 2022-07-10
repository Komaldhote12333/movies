from django.contrib import admin
from .models import * 


class movieslist(admin.ModelAdmin):
    list_display = ["name" , "downloadlink", "movitype"]












admin.site.register(Category)
admin.site.register(Movie,movieslist)
admin.site.register(Team)