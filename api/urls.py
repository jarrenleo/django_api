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

# Configure Swagger/OpenAPI documentation view with API metadata
schema_view = get_schema_view(
    openapi.Info(
        title="Steam Games API",
        default_version="v1",
        description="Python version: 3.13.0\nDjango version: 5.1.4\nPackages used: asgiref, djangorestframework, drf-yasg, gunicorn, inflection, packaging, python-dotenv, pytz, PyYAML, sqlparse, tzdata, uritemplate, whitenoise\nUsername: jaleo\nPassword: 1234567890",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# API endpoints
urlpatterns = [
    # Game CRUD operations
    path(
        "api/game/", get_game, name="get_game"
    ),  # GET - Retrieve single game by ID or name
    path(
        "api/game/create/", create_game, name="create_game"
    ),  # POST - Create new game entry
    path(
        "api/game/update/", update_game, name="update_game"
    ),  # PATCH - Update existing game
    path(
        "api/game/delete/", delete_game, name="delete_game"
    ),  # DELETE - Remove game entry
    path(
        "api/games/", get_games, name="get_games"
    ),  # GET - List games with filtering and pagination
    path(
        "api/games/recommend/", get_recommended_games, name="get_recommended_games"
    ),  # GET - Get recommended games
    # API Documentation endpoints
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),  # Raw OpenAPI/Swagger JSON schema
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),  # Interactive Swagger UI documentation interface
    path(
        "redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),  # Alternative ReDoc documentation interface
]
