from django.urls import path
from .views import api_home
from .api import (
    get_game,
    get_recommended_games,
    get_games,
    create_game,
    update_game,
    delete_game,
)

urlpatterns = [
    path("", api_home, name="api_home"),
    path("api/game/", get_game, name="get_game"),
    path("api/games/", get_games, name="get_games"),
    path("api/games/recommend/", get_recommended_games, name="get_recommended_games"),
    path("api/games/create/", create_game, name="create_game"),
    path("api/games/update/<int:pk>", update_game, name="update_game"),
    path("api/games/delete/<int:pk>", delete_game, name="delete_game"),
]
