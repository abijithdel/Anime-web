from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('animes/',views.anime, name='animes'),
    path('movies/',views.movies, name='movies'),
    path('category/',views.category, name='category'),
    path('video/<pk>/<foo>',views.video, name='video'),
    path('category/<str:foo>',views.category_one, name='category_sp'),
    path('search/',views.search, name='search'),
]