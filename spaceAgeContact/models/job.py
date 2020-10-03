from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.title
