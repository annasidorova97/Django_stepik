from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def main_page(request):
    return HttpResponse('Главная страница')


def posts(request):
    return HttpResponse('Все посты блога')


def get_info_about_post(request, post_name):
    return HttpResponse(f'Информация о посте {post_name}')


def get_info_about_post_by_number(request, number_post: int):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')

