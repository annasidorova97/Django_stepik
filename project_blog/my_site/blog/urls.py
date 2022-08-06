from django.urls import path
from . import views

urlpatterns = [
    path('<post_name>/', views.get_info_about_post)
]