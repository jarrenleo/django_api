from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
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
from datetime import datetime
from decimal import Decimal


class GameAPITests(TestCase):
    """Set up test data before each test method."""

    def setUp(self):
        self.client = APIClient()

        # Create test instances of related models
        self.language = SupportedLanguage.objects.create(supported_language="English")
        self.audio_language = FullAudioLanguage.objects.create(
            full_audio_language="English"
        )
        self.developer = Developer.objects.create(developer="Developer")
        self.publisher = Publisher.objects.create(publisher="Publisher")
        self.category = Category.objects.create(category="Category")
        self.genre = Genre.objects.create(genre="Genre")
        self.tag = Tag.objects.create(tag="Tag")

        # Create two test game instances with minimal required data
        self.game1 = Game.objects.create(
            name="Test Game 1",
            release_date=datetime(2020, 1, 1),
            price=Decimal("29.99"),
        )

        self.game2 = Game.objects.create(
            name="Test Game 2",
            release_date=datetime(2021, 1, 1),
            price=Decimal("39.99"),
        )

    """Test retrieving list of all games."""

    def test_get_games_list(self):
        response = self.client.get(reverse("get_games"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    """Test retrieving a single game by ID or name."""

    def test_get_single_game(self):
        # Test existing game by ID
        response = self.client.get(reverse("get_game"), {"id": self.game1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Game 1")

        # Test existing game by name
        response = self.client.get(reverse("get_game"), {"name": "Test Game 1"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Game 1")

        # Test non-existent game
        response = self.client.get(reverse("get_game"), {"id": 999})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Test missing parameters
        response = self.client.get(reverse("get_game"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    """Test retrieving recommended games based on a reference game."""

    def test_get_recommended_games(self):
        # Test recommendations by ID
        url = f"{reverse('get_recommended_games')}?id={self.game1.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["reference_game"]["name"], "Test Game 1")
        self.assertIn("recommended_games", response.data)

        # Test recommendations by name
        url = f"{reverse('get_recommended_games')}?name=Test Game 1"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["reference_game"]["name"], "Test Game 1")

        # Test non-existent game
        url = f"{reverse('get_recommended_games')}?id=999"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Test missing parameters
        response = self.client.get(reverse("get_recommended_games"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    """Test filtering games by specific criteria."""

    def test_filtered_games(self):
        response = self.client.get(reverse("get_games"), {"filterBy": "year(2020)"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], "Test Game 1")

    """Test sorting games by specific fields."""

    def test_sorted_games(self):
        response = self.client.get(
            reverse("get_games"), {"sortBy": "price", "sortOrder": "desc"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["name"], "Test Game 2")

    """Test creating a new game with valid data."""

    def test_create_game(self):
        initial_count = Game.objects.count()

        # Prepare complete game data payload
        payload = {
            "name": "Test Game 3",
            "release_date": "2024-12-12",
            "estimated_owners": 0,
            "peak_concurrent_users": 0,
            "required_age": 0,
            "price": "29.99",
            "dlc_count": 0,
            "about_the_game": "Test about the game",
            "supported_languages": ["English"],
            "full_audio_languages": ["English"],
            "header_image": "https://example.com/header.jpg",
            "website": "https://example.com",
            "support_url": "https://example.com/support",
            "support_email": "support@example.com",
            "windows": True,
            "mac": False,
            "linux": False,
            "metacritic_score": 80,
            "metacritic_url": "https://example.com/metacritic",
            "positive_ratings": 0,
            "negative_ratings": 0,
            "achievements": 0,
            "average_playtime": 0,
            "median_playtime": 0,
            "developers": ["Developer"],
            "publishers": ["Publisher"],
            "genres": ["Genre"],
            "categories": ["Category"],
            "tags": ["Tag"],
        }

        response = self.client.post(reverse("create_game"), data=payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), initial_count + 1)
        game = Game.objects.last()
        self.assertEqual(game.name, "Test Game 3")
        self.assertEqual(game.price, Decimal("29.99"))

        # Verify relationships were created correctly
        self.assertEqual(game.developers.count(), 1)
        self.assertEqual(game.publishers.count(), 1)
        self.assertEqual(game.genres.count(), 1)
        self.assertEqual(game.categories.count(), 1)
        self.assertEqual(game.tags.count(), 1)

    """Test creating a game with invalid data."""

    def test_create_game_invalid_data(self):
        initial_count = Game.objects.count()

        payload = {
            "price": "invalid_price",
            "peak_concurrent_users": "not_an_integer",
        }

        response = self.client.post(reverse("create_game"), payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Game.objects.count(), initial_count)
        self.assertIn("name", response.data)
        self.assertIn("release_date", response.data)

    """Test updating an existing game."""

    def test_update_game(self):
        # Send ID as query param, update data as body
        update_data = {"name": "Updated Game Name"}
        url = f"{reverse('update_game')}?id={self.game1.id}"
        response = self.client.patch(url, data=update_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["game"]["name"], "Updated Game Name")

    """Test deleting games with various scenarios."""

    def test_delete_game(self):
        # Test deleting existing game
        url = f"{reverse('delete_game')}?id={self.game1.id}"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Game.objects.count(), 1)

        # Test deleting non-existent game
        url = f"{reverse('delete_game')}?id=999"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Test missing parameters
        response = self.client.delete(reverse("delete_game"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
