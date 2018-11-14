from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Game
from users.models import CustomUser


class IndexView(ListView):
    template_name = 'games/index.html'
    context_object_name = 'latest_games_news'

    def get_queryset(self):
        """Return the last five added or modified games"""
        return Game.objects.all().order_by('-mod_date')[:5]


class GameView(DetailView):
    model = Game
    template_name = 'games/detail.html'
