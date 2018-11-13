from django.shortcuts import render
from django.views import generic

from .models import Game


class DetailView(generic.DetailView):
    model = Game
    template_name = 'games/detail.html'
