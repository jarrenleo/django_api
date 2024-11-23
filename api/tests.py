from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Game
from datetime import datetime

class GameAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create some test data
        self.game1 = Game.objects.create(
            name="Test Game 1",
            release_date=datetime(2020, 1, 1),
            metacritic_score=85
        )
        self.game2 = Game.objects.create(
            name="Test Game 2",
            release_date=datetime(2021, 1, 1),
            metacritic_score=90
        )

    def test_get_games_list(self):
        response = self.client.get(reverse('get_games'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_get_single_game(self):
        # Test existing game
        response = self.client.get(reverse('get_game', args=[self.game1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Game 1')

        # Test non-existent game
        response = self.client.get(reverse('get_game', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_top_rated_games(self):
        response = self.client.get(reverse('get_top_rated_games'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], 'Test Game 2')  # Higher rated game should be first

    def test_get_games_by_year(self):
        response = self.client.get(reverse('get_games_by_year', args=[2020]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'Test Game 1')

    def test_create_game(self):
        new_game_data = {
            'name': 'New Test Game',
            'release_date': '2023-01-01',
            'metacritic_score': 88
        }
        response = self.client.post(reverse('create_game'), new_game_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 3)

    def test_create_game_invalid_data(self):
        invalid_game_data = {
            'name': '',  # Name should not be empty
            'release_date': '2023-01-01',
            'metacritic_score': 88
        }
        response = self.client.post(reverse('create_game'), invalid_game_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_game(self):
        update_data = {'name': 'Updated Game Name'}
        response = self.client.patch(reverse('update_game', args=[self.game1.id]), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Game Name')

    def test_delete_game(self):
        # Test deleting existing game
        response = self.client.delete(reverse('delete_game', args=[self.game1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Game.objects.count(), 1)

        # Test deleting non-existent game
        response = self.client.delete(reverse('delete_game', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
