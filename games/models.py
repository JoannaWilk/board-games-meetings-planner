from django.db import models


class Game(models.Model):

    name = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    min_players = models.IntegerField(default=1)
    max_players = models.IntegerField(default=99)

    def __str__(self):
        return self.name
