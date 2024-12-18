from rest_framework import serializers
from .models import (
    SupportedLanguage,
    FullAudioLanguage,
    Developer,
    Publisher,
    Category,
    Genre,
    Tag,
    Game,
)

"""
Serializer for the Game model that handles conversion between Game instances and JSON.

This serializer includes all fields from the Game model and handles related fields using
SlugRelatedFields for better readability in the API responses.

Attributes:
    supported_languages: Languages supported in the game's interface
    full_audio_languages: Languages with full audio dubbing
    developers: Game development studios
    publishers: Game publishing companies
    categories: Steam categories (e.g., Single-player, Multi-player)
    genres: Game genres (e.g., Action, RPG)
    tags: User-defined tags describing the game
"""


class GameSerializer(serializers.ModelSerializer):
    # Define related fields using SlugRelatedField for readable string representation
    supported_languages = serializers.SlugRelatedField(
        many=True,
        slug_field="supported_language",
        queryset=SupportedLanguage.objects.all(),
    )
    full_audio_languages = serializers.SlugRelatedField(
        many=True,
        slug_field="full_audio_language",
        queryset=FullAudioLanguage.objects.all(),
    )
    developers = serializers.SlugRelatedField(
        many=True, slug_field="developer", queryset=Developer.objects.all()
    )
    publishers = serializers.SlugRelatedField(
        many=True, slug_field="publisher", queryset=Publisher.objects.all()
    )
    categories = serializers.SlugRelatedField(
        many=True, slug_field="category", queryset=Category.objects.all()
    )
    genres = serializers.SlugRelatedField(
        many=True, slug_field="genre", queryset=Genre.objects.all()
    )
    tags = serializers.SlugRelatedField(
        many=True, slug_field="tag", queryset=Tag.objects.all()
    )

    """Meta class defining the model and fields for serialization."""

    class Meta:
        model = Game
        fields = [
            "id",
            "name",
            "release_date",
            "estimated_owners",
            "peak_concurrent_users",
            "required_age",
            "price",
            "dlc_count",
            "about_the_game",
            "supported_languages",
            "full_audio_languages",
            "header_image",
            "website",
            "support_url",
            "support_email",
            "windows",
            "mac",
            "linux",
            "metacritic_score",
            "metacritic_url",
            "positive_ratings",
            "negative_ratings",
            "achievements",
            "average_playtime",
            "median_playtime",
            "developers",
            "publishers",
            "categories",
            "genres",
            "tags",
        ]
