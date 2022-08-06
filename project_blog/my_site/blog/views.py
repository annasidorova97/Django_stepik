from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def main_page(request):
    return HttpResponse('Главная страница')


def posts(request):
    return HttpResponse('Все посты блога')


def get_info_about_post(request, post_name):
    return HttpResponse(f'Информация о посте {post_name}')

