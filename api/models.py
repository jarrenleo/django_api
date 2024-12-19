from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

"""Model representing a language supported by a game."""


class SupportedLanguage(models.Model):
    supported_language = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.supported_language


"""Model representing a language with full audio support in a game."""


class FullAudioLanguage(models.Model):
    full_audio_language = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.full_audio_language


"""Model representing a game developer company."""


class Developer(models.Model):
    developer = models.CharField(max_length=255, unique=True, null=False)

    def __str__(self):
        return self.developer


"""Model representing a game publisher company."""


class Publisher(models.Model):
    publisher = models.CharField(max_length=255, unique=True, null=False)

    def __str__(self):
        return self.publisher


"""Model representing a game category (e.g., Single-player, Multi-player)."""


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.category


"""Model representing a game genre (e.g., Action, RPG, Strategy)."""


class Genre(models.Model):
    genre = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.genre


"""Model representing a user-defined tag for a game."""


class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.tag


"""
Model representing a video game with its detailed information.

This model stores comprehensive information about a video game, including:
- Basic details (name, release date, price)
- Platform compatibility (Windows, Mac, Linux)
- Player statistics (estimated owners, peak users, playtime)
- Content information (age requirement, DLC count)
- Ratings and reviews (Metacritic score, positive/negative ratings)
- Support information (website, support URLs, languages)
- Related entities (developers, publishers, genres, etc.)
"""


class Game(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.TextField(null=False)
    release_date = models.DateField(null=False)
    estimated_owners = models.IntegerField(null=True, validators=[MinValueValidator(0)])
    peak_concurrent_users = models.IntegerField(
        null=True, validators=[MinValueValidator(0)]
    )
    required_age = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(21)]
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    dlc_count = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    about_the_game = models.TextField(null=True)
    supported_languages = models.ManyToManyField(SupportedLanguage, blank=True)
    full_audio_languages = models.ManyToManyField(FullAudioLanguage, blank=True)
    header_image = models.URLField(null=True)
    website = models.URLField(null=True)
    support_url = models.URLField(null=True)
    support_email = models.EmailField(null=True)
    windows = models.BooleanField(default=False)
    mac = models.BooleanField(default=False)
    linux = models.BooleanField(default=False)
    metacritic_score = models.IntegerField(
        null=True, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    metacritic_url = models.URLField(null=True)
    positive_ratings = models.IntegerField(null=True, validators=[MinValueValidator(0)])
    negative_ratings = models.IntegerField(null=True, validators=[MinValueValidator(0)])
    achievements = models.IntegerField(null=True, validators=[MinValueValidator(0)])
    average_playtime = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    median_playtime = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    developers = models.ManyToManyField(Developer, blank=True)
    publishers = models.ManyToManyField(Publisher, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
