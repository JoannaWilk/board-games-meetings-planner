from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from .models import Contribution, Game
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
        if request.POST['name']:
            game = Game()
            game.name = request.POST['name']
            if request.POST['min_players']:
                game.min_players = request.POST['min_players']
            if request.POST['max_players']:
                game.max_players = request.POST['max_players']
            if request.POST['description']:
                game.description = request.POST['description']
            game.save()
            contribution = Contribution(
                game=game, user=request.user,
                type='added', mod_date=game.pub_date
            )
            contribution.save()
            return redirect('games:home')
        else:
            return render(
                request, 'games/add.html',
                {'error': 'ERROR: You must give a name of the game to add it.'})
    else:
        return render(request, 'games/add.html')
