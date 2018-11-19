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
    mod_date = models.DateTimeField(auto_now=True)
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    game_type = models.CharField(max_length=1, choices=GAME_TYPES)
    description = models.TextField(null=True)

    # todo remove null=True from added_by and last_modified_by
    added_by = models.ForeignKey(
        CustomUser, on_delete=models.SET('deleted'),
        related_name='added_games')
    last_modified_by = models.ForeignKey(
        CustomUser, on_delete=models.SET('deleted'),
        related_name='modified_games')
    contributors = models.ManyToManyField(
        CustomUser, related_name='contributed_to')
    owners = models.ManyToManyField(CustomUser, related_name='owned_games')

    def __str__(self):
        return self.name
