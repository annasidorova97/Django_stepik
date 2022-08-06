from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def get_rectangle_area(request, width, height):
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def get_square_area(request, width):
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width ** 2}')


def get_circle_area(request, radius):
    return HttpResponse(f'Площадь круга радиуса {radius} равна {3.14 * radius * radius}')


def redirect_get_rectangle_area(request, width, height):
    redirect_url = reverse('rectangle', args=[width, height])
    return HttpResponseRedirect(redirect_url)


def redirect_get_square_area(request, width):
    redirect_url = reverse('square', args=[width])
    return HttpResponseRedirect(redirect_url)


def redirect_get_circle_area(request, radius):
    redirect_url = reverse('circle', args=[radius])
    return HttpResponseRedirect(redirect_url)
