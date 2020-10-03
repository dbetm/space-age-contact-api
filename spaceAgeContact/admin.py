from django.contrib import admin
from .models.user import User
from .models.job import Job
from .models.school import School
from .models.team import Team
from .models.game_topic import GameTopic
from .models.game import Game
# Register your models here.
admin.site.register(User)
admin.site.register(School)
admin.site.register(Job)
admin.site.register(Team)
admin.site.register(GameTopic)
admin.site.register(Game)
