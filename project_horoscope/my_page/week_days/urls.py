from django.urls import path
from . import views

urlpatterns = [
    path('<week_day>/', views.get_list_of_tasks_by_day)
]