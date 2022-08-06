from django.urls import path
from . import views

urlpatterns = [
    path('<int:zodiac_sign>', views.get_info_by_number_zodiac_sign),
    path('<str:zodiac_sign>', views.get_info_by_zodiac_sign)
]
