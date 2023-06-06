from django.db import models
from django.contrib.auth.models import User


class Week(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    archived = models.BooleanField(default=0)

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=100)
    md = models.IntegerField(default=0)
    td = models.IntegerField(default=0)
    wd = models.IntegerField(default=0)
    th = models.IntegerField(default=0)
    fr = models.IntegerField(default=0)
    st = models.IntegerField(default=0)
    sd = models.IntegerField(default=0)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
