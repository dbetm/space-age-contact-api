from django.db import models
from .user import User
from .game_topic import GameTopic

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    topic = models.ForeignKey(GameTopic, on_delete=models.CASCADE)
    total_space_dust = models.IntegerField()
    duration = models.IntegerField()
    num_correct_answers = models.IntegerField()
    players = models.ManyToManyField(User)

    def __str__(self):
        return self.title
