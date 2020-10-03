from django.db import models


class School(models.Model):
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    field = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.degree
