from django.urls import path
from . import views

urlpatterns = [
    path('<zodiac_sign>/', views.get_info_by_zodiac_sign)
]
