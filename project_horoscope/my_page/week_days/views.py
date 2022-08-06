from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def monday(request):
    return HttpResponse('Список дел на понедельник')


def tuesday(request):
    return HttpResponse('Список дел на вторник')


def wednesday(request):
    return HttpResponse('Список дел на среду')


def thursday(request):
    return HttpResponse('Список дел на четверг')


def friday(request):
    return HttpResponse('Список дел на пятницу')


def saturday(request):
    return HttpResponse('Список дел на субботу')


def sunday(request):
    return HttpResponse('Список дел на воскресенье')