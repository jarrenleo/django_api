from django.urls import path
from .views import get_games, get_game, get_top_rated_games, get_games_by_year,create_game, update_game, delete_game

urlpatterns = [
    path('games/', get_games, name='get_games'),
    path('games/<int:pk>/', get_game, name='get_game'),
    path('games/top-rated/', get_top_rated_games, name='get_top_rated'),
    path('games/year/<int:year>/', get_games_by_year, name='get_games_by_year'),
    path('games/create/', create_game, name='create_game'),
    path('games/update/<int:pk>', update_game, name='update_game'),
    path('games/delete/<int:pk>', delete_game, name='delete_game'),
]