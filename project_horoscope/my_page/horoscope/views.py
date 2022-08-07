from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

zodiac_dict = {
    'aries': ['Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).', 'fire'],
    'taurus': ['Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).', 'earth'],
    'gemini': ['Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).', 'air'],
    'cancer': ['Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).', 'water'],
    'leo': ['Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).', 'fire'],
    'virgo': ['Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).', 'earth'],
    'libra': ['Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).', 'air'],
    'scorpio': ['Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).', 'water'],
    'sagittarius': ['Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).', 'fire'],
    'capricorn': ['Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).', 'earth'],
    'aquarius': ['Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).', 'air'],
    'pisces': ['Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).', 'water']
}


elements = ['fire', 'earth', 'air', 'water']


def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ''
    for zodiac in zodiacs:
        redirect_path = reverse('horoscope_name', args=[zodiac])
        li_elements += f"<li><a href='{redirect_path}'>{zodiac.title()} </a> </li>"
    response = f'<ol> {li_elements} </ol>'
    return HttpResponse(response)


def types(request):
    li_elements = ''
    for element in elements:
        redirect_path = reverse('zodiac_by_elements', args=[element])
        li_elements += f"<li> <a href='{redirect_path}'> {element.title()} </a> </li>"
    response = f"<ul> {li_elements} </ul>"
    return HttpResponse(response)


def get_zodiacs_by_type_of_element(request, element):
    element_list = []
    for zodiac in list(zodiac_dict.items()):
        if element == zodiac[1][1]:
            element_list.append(zodiac[0])
    li_elements = ''
    for zod in element_list:
        redirect_path = reverse('horoscope_name', args=[zod])
        li_elements += f"<li> <a href='{redirect_path}'> {zod.title()} <a> </li>"
    response = f"<ul> {li_elements} </ul>"
    return HttpResponse(response)


def get_info_by_zodiac_sign(request, zodiac_sign: str):
    description = zodiac_dict.get(zodiac_sign)
    if description:
        return HttpResponse(description[0])
    else:
        return HttpResponseNotFound(f'{zodiac_sign} - unknown zodiac sign')


def get_info_by_number_zodiac_sign(request, zodiac_sign: int):
    if zodiac_sign > len(list(zodiac_dict)):
        return HttpResponseNotFound(f'{zodiac_sign} - false number of zodiac sign')
    zodiac_name = list(zodiac_dict)[zodiac_sign - 1]
    redirect_url = reverse('horoscope_name', args=[zodiac_name])
    return HttpResponseRedirect(redirect_url)

