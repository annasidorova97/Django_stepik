from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.


def get_rectangle_area(request, width, height):
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def get_square_area(request, width):
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width ** 2}')


def get_circle_area(request, radius):
    return HttpResponse(f'Площадь круга радиуса {radius} равна {3.14 * radius * radius}')


def redirect_get_rectangle_area(request, width, height):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')


def redirect_get_square_area(request, width):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}')


def redirect_get_circle_area(request, radius):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')