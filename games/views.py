from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
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


@login_required(login_url='users/login/')
def add_game(request):
    if request.method == 'POST':
        # name, min_players, max_players
        if request.POST['name']:
            game = Game()
            game.name = request.POST['name']
            game.added_by = request.user
            if request.POST['min_players']:
                game.min_players = request.POST['min_players']
            if request.POST['max_players']:
                game.max_players = request.POST['max_players']
            game.save()
            return redirect('games:home')
        else:
            return render(
                request, 'games/add.html',
                {'error': 'ERROR: You must give a name of the game to add it.'})
    else:
        return render(request, 'games/add.html')
