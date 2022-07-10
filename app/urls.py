from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
   # path('search',views.search, name="search"),
   path('total', views.total, name="total"),
   path('searchmov', views.searchmov, name="searchmov"),    
   path('team', views.team, name="team") 
]