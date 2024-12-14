from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .api import (
    get_game,
    get_recommended_games,
    get_games,
    create_game,
    update_game,
    delete_game,
)

# Configure Swagger/OpenAPI documentation view
schema_view = get_schema_view(
    openapi.Info(
        title="Steam Games API",
        default_version="v1",
        description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# API endpoints
urlpatterns = [
    # Game CRUD operations
    path("api/game/", get_game, name="get_game"),  # Get single game by ID or name
    path("api/games/", get_games, name="get_games"),  # Get list of games with filtering
    path(
        "api/games/recommend/", get_recommended_games, name="get_recommended_games"
    ),  # Get game recommendations
    path("api/game/create/", create_game, name="create_game"),  # Create new game
    path("api/game/update/", update_game, name="update_game"),  # Update existing game
    path("api/game/delete/", delete_game, name="delete_game"),  # Delete existing game
    # API Documentation endpoints
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),  # Raw OpenAPI schema
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),  # Swagger UI documentation
    path(
        "redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),  # ReDoc documentation
]
