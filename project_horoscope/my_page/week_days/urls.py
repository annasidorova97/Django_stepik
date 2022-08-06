from django.urls import path
from . import views

urlpatterns = [
    path('<int:week_day>', views.get_list_of_tasks_by_number),
    path('<str:week_day>', views.get_list_of_tasks_by_day, name='week_day')
]