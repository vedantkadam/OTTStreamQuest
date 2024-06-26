from django.contrib import admin
from django.urls import path
from . import views

app_name = 'movies_name'

urlpatterns = [
    path('', views.tp, name="movie_list"),
    path('added_plans/', views.added_plans, name="added_plans"),
    path('movie_list/', views.movie_list, name="movie_list"),
    path('details/<int:pk>',  views.movie_detail, name="movie_detail"),
    path('get_popular/<int:start>/<int:finish>', views.get_popular, name="get_popular"),
    path('get_top/<int:start>/<int:finish>', views.get_top, name="get_top"),
    path('get_movie/<int:pk>', views.get_movie, name="get_movie"),
    path('get_movie_tmdb/<int:tmdb>', views.get_movie_tmdb, name="get_movie_tmdb"),
    path('search/<str:term>', views.search, name="search"),
    path('getSearch/<str:term>', views.getSearch, name="getSearch"),
    path('keyword/<str:keyword_name>', views.keyword, name="keyword"),
    path('getKeyword/<str:keyword_name>', views.getKeyword, name="getKeyword"),
    path('director/<str:director_name>', views.director, name="director"),
    path('getDirector/<str:director_name>', views.getDirector, name="getDirector"),
    path('get_similar/<int:pk>', views.get_similar, name="get_similar"),
    path('collabRecommendation/<int:tmdb_id>', views.collabRecommendation, name="collabRecommendation"),
    path('getRating/<int:tmdb_id>', views.getRating, name="getRating"),
    path('addRating/<int:tmdb_id>/<int:rating>', views.addRating, name="addRating"),
    path('removeRating/<int:tmdb_id>', views.removeRating, name="removeRating"),
    path('checkIfInWatchlist/<int:tmdb_id>', views.checkIfInWatchlist, name="checkIfInWatchlist"),
    path('addToWatchlist/<int:user_id>/<int:tmdb_id>', views.addToWatchlist, name="addToWatchlist"),
    path('addToList/<int:user_id>/<int:tmdb_id>/<int:list_id>', views.addTolist, name="addTolist"),
    path('plans/', views.plans),
    path("e/<int:id>/", views.single_ott, name="plans"),
    path('booking/<int:id>', views.booking, name="booking"),
    path('receipt', views.receipt, name='receipt'),
    path('confirm_booking', views.confirm_booking, name='confirm_booking'),
    path('planbuy', views.planbuy, name="planbuy"),
    path('contact', views.contact, name="contact"),
] 

