from django.db import models
from django.utils import timezone

from users.models import CustomUser


class Game(models.Model):

    name = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    min_players = models.IntegerField(default=1)
    max_players = models.IntegerField(default=99)
    owners = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.name
