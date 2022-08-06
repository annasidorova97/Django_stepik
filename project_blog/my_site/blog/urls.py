from django.urls import path
from . import views

urlpatterns = [
    path('<int:number_post>/', views.get_info_about_post_by_number),
    path('<post_name>/', views.get_info_about_post)
]