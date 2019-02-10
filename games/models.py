from django.db import models

from users.models import CustomUser


class Game(models.Model):

    name = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    description = models.TextField(null=True)
    added_by = models.ForeignKey(CustomUser, on_delete=models.SET('deleted'),
                                 null=True)
    owners = models.ManyToManyField(CustomUser, related_name='owned_games')

    def __str__(self):
        return self.name
