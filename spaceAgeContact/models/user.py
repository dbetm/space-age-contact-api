from django.db import models
from django_countries.fields import CountryField
from .school import School
from .job import Job


class User(models.Model):
    profile_pic = models.ImageField()
    name = models.CharField(max_length=200)
    birthdate = models.DateField()
    country = CountryField()
    education = models.ManyToManyField(School)
    work = models.ManyToManyField(Job)
    motto = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    points = models.IntegerField()

    def __str__(self):
        return self.name
