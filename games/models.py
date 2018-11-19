from django.db import models

from users.models import CustomUser


class Game(models.Model):

    GAME_TYPES = (
        ('SG', 'Strategy'),
        ('DB', 'Deck Building'),
        ('AG', 'Adventures'),
    )

    name = models.CharField(max_length=300, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    type = models.CharField(max_length=1, choices=GAME_TYPES)
    description = models.TextField(null=True)

    added_by = models.ForeignKey(CustomUser, on_delete=models.SET('deleted'))

    contributors = models.ManyToManyField(
        CustomUser, related_name='contributed_to',
        through='Contribution'
    )
    owners = models.ManyToManyField(CustomUser, related_name='owned_games')

    def __str__(self):
        return self.name


class Contribution(models.Model):

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.SET('deleted'))
    type = models.CharField(max_length=10)
    mod_date = models.DateTimeField(auto_now_add=True)
