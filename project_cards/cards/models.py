from django.db import models


class Stack(models.Model):
    name = models.CharField(max_length=120, unique=True)


class Group(models.Model):
    interval = models.PositiveSmallIntegerField()


class Card(models.Model):
    question = models.CharField(max_length=140)
    answer = models.CharField(max_length=280)
    picture_id = models.CharField(max_length=100, null=True, default='NULL')
    counter = models.SmallIntegerField(default=0)
    last_show = models.DateField(auto_now=True)
    stack_id = models.ForeignKey(Stack, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
