from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

week_dict = {
    'monday': 'Список дел на понедельник',
    'tuesday': 'Список дел на вторник',
    'wednesday': 'Список дел на среду',
    'thursday': 'Список дел на четверг',
    'friday': 'Список дел на пятницу',
    'saturday': 'Список дел на субботу',
    'sunday': 'Список дел на воскресенье',
}


def get_list_of_tasks_by_day(request, week_day: str):
    task_of_day = week_dict.get(week_day)
    if task_of_day:
        return HttpResponse(task_of_day)
    else:
        return HttpResponseNotFound (f'Unknown day of the week {week_day}')


def get_list_of_tasks_by_number(request, week_day: int):
    if week_day > len(list(week_dict)):
        return HttpResponseNotFound(f'Неверный номер дня - {week_day}')
    day = list(week_dict)[week_day - 1]
    return HttpResponseRedirect(f'/todo_week/{day}')

