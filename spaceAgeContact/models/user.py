from django.db import models
from django_countries.fields import CountryField
from .school import School
from .job import Job


class User(models.Model):
    profile_pic = models.ImageField(blank=True)
    name = models.CharField(max_length=200)
    birthdate = models.DateField()
    country = CountryField()
    education = models.ManyToManyField('School', related_name='students', blank=True)
    work = models.ManyToManyField('Job', related_name='workers', blank=True)
    motto = models.CharField(max_length=300, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    points = models.IntegerField(default=0)
    following = models.ManyToManyField('User', related_name='followings', blank=True)
    followers = models.ManyToManyField('User', related_name='follower', blank=True)

    def __str__(self):
        return self.name
