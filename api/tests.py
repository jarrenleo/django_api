from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Game
from datetime import datetime
from decimal import Decimal


class GameAPITests(TestCase):
    """Set up test data before each test method"""

    def setUp(self):
        self.client = APIClient()
        # Create two test game instances with minimal required data
        self.game1 = Game.objects.create(
            name="Test Game 1",
            release_date=datetime(2020, 1, 1),
            metacritic_score=85,
            peak_ccu=1000,
        )
        self.game2 = Game.objects.create(
            name="Test Game 2",
            release_date=datetime(2021, 1, 1),
            metacritic_score=90,
            peak_ccu=2000,
        )

    """Test retrieving list of all games"""

    def test_get_games_list(self):
        response = self.client.get(reverse("get_games"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    """Test retrieving a single game by ID and name"""

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

    """Test getting game recommendations based on a reference game"""

    def test_get_recommended_games(self):
        # Test recommendations by ID
        response = self.client.get(
            reverse("get_recommended_games"), {"id": self.game1.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["reference_game"]["name"], "Test Game 1")
        self.assertIn("similar_games", response.data)

        # Test recommendations by name
        response = self.client.get(
            reverse("get_recommended_games"), {"name": "Test Game 1"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["reference_game"]["name"], "Test Game 1")

        # Test non-existent game
        response = self.client.get(reverse("get_recommended_games"), {"id": 999})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """Test filtering games by release year"""

    def test_filtered_games(self):
        response = self.client.get(reverse("get_games"), {"filterBy": "year(2020)"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], "Test Game 1")

    """Test sorting games by metacritic score"""

    def test_sorted_games(self):
        response = self.client.get(
            reverse("get_games"), {"sortBy": "metacriticScore", "sortOrder": "desc"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["name"], "Test Game 2")

    def test_create_game(self):
        initial_count = Game.objects.count()  # Get count before creating new game

        payload = {
            "name": "Test Game",
            "release_date": "2024-03-20",
            "estimated_owners": "0-20000",
            "peak_ccu": 100,
            "required_age": 18,
            "price": "29.99",
            "dlc_count": 2,
            "about_the_game": "This is a test game",
            "windows": True,
            "mac": False,
            "linux": False,
            "genres": "Action,Adventure",
            "tags": "Multiplayer,RPG",
        }

        response = self.client.post(reverse("create_game"), payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Game.objects.count(), initial_count + 1
        )  # Check that count increased by 1
        game = Game.objects.last()
        self.assertEqual(game.name, "Test Game")
        self.assertEqual(game.price, Decimal("29.99"))
        self.assertEqual(game.genres, "Action,Adventure")

    """Test creating a game with invalid data"""

    def test_create_game_invalid_data(self):
        initial_count = Game.objects.count()  # Get count before attempting to create

        payload = {
            # Missing required 'name' field
            "price": "invalid_price",
            "peak_ccu": "not_an_integer",
        }

        response = self.client.post(reverse("create_game"), payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Game.objects.count(), initial_count)  # Count should not change
        self.assertIn("name", response.data)  # Should contain name field error
        self.assertIn("price", response.data)  # Should contain price field error
        self.assertIn("peak_ccu", response.data)  # Should contain peak_ccu field error

    """Test updating an existing game"""

    def test_update_game(self):
        update_data = {"name": "Updated Game Name"}
        response = self.client.patch(
            reverse("update_game", args=[self.game1.id]), update_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Game Name")

    """Test deleting existing and non-existent games"""

    def test_delete_game(self):
        # Test deleting existing game
        response = self.client.delete(reverse("delete_game", args=[self.game1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Game.objects.count(), 1)

        # Test deleting non-existent game
        response = self.client.delete(reverse("delete_game", args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
