from django.db import models

from django.contrib.auth.models import User


class Chapter(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=20, default='')
    image_url = models.CharField(max_length=100, default='', blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Stack(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=20, default='')
    image_url = models.CharField(max_length=100, default='NULL')
    chapter_id = models.ForeignKey(
        Chapter, on_delete=models.CASCADE)
    # ДОБАВИТЬ: прогресс раздела — в БД?
    # ДОБАВИТЬ: связь многие-ко-многим с таблицей User


class Group(models.Model):
    interval = models.PositiveSmallIntegerField()

    @property
    def name(self):
        return f'Группа {self.pk}'


class Card(models.Model):
    question = models.CharField(max_length=140)
    answer = models.CharField(max_length=280)
    picture_url = models.CharField(max_length=100, null=True, default='NULL')
    counter = models.PositiveSmallIntegerField(default=0)
    last_show = models.DateField(auto_now=True)
    stack_id = models.ForeignKey(Stack, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __validate_group_id(self) -> bool:
        """Проверяет, принадлежит ли вычисленный group_id реальным pk объектов групп."""
