from django.test import TestCase
from django.urls import reverse

from .models import Game
from .views import add_game

# testowanie user profilu - logowanie, rejestracja
# testowanie dodanych gier - nie dodawać tych samych
# dodawanie bez tytułu, dodawanie bez innych parametrów


def create_game(game_name):
    """Create a game with a given 'game_name'"""
    return Game.objects.create(name=game_name)


def set_min_players_number(game, min_players):
    """Set a min_players number for a given game"""
    game.min_players = min_players
    game.save()
    return game


class GameIndexViewTests(TestCase):

    def test_two_games(self):
        """The game index page displays multiple games
        in an order based on last modifications.
        Any of the game wasn't modified."""
        create_game(game_name='Game 1.')
        create_game(game_name='Game 2.')
        response = self.client.get(reverse('games:home'))
        self.assertQuerysetEqual(
            response.context['latest_games_news'],
            ['<Game: Game 2.>', '<Game: Game 1.>']
        )

    def test_two_games_one_modified_later(self):
        """The game index page displays multiple games
        in an order based on last modifications.
        Firstly created game is modified after adding the second one."""
        first_game = create_game(game_name='Game 1.')
        create_game(game_name='Game 2.')
        set_min_players_number(first_game, 2)
        response = self.client.get(reverse('games:home'))
        self.assertQuerysetEqual(
            response.context['latest_games_news'],
            ['<Game: Game 1.>', '<Game: Game 2.>']
        )
