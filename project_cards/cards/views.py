from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Chapter, Stack, Card, Group


def main(request):
    chapter_list = Chapter.objects.all()
    pages = len(chapter_list) // 20  # TODO: Переделать на нормальный пагинатор

    template = loader.get_template('cards/main.html')

    context = {
        'chapter_list': chapter_list,
        'pages': pages
    }

    return HttpResponse(template.render(context, request))


def chapter(request):
    pass


def stack(request):
    pass


def train(request):
    pass
