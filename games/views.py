from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from .forms import AddGameForm
from .models import Contribution, Game
from users.models import CustomUser


class IndexView(ListView):
    template_name = 'games/index.html'
    context_object_name = 'latest_games_news'

    def get_queryset(self):
        """Return the last five added or modified games"""
        return Game.objects.all().order_by('-pub_date')[:5]


class GameView(DetailView):
    model = Game
    template_name = 'games/detail.html'


@login_required(login_url='users/login/')
def add_game(request):
    if request.method == 'POST':
        form = AddGameForm(request.POST)
        if form.is_valid():
            game = Game()
            game.name = form.cleaned_data['name']
            game.min_players = form.cleaned_data['min_players']
            game.max_players = form.cleaned_data['max_players']
            game.added_by = request.user
            game.save()
            contribution = Contribution(
                game=game, user=request.user,
                type='added', mod_date=game.pub_date)
            contribution.save()
            return redirect('games:home')
    else:
        form = AddGameForm()

    return render(request, 'games/add.html', {'form': form})
