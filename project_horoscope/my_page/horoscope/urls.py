from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type', views.types),
    path('type/<str:element>', views.get_zodiacs_by_type_of_element, name='zodiac_by_elements'),
    path('<int:zodiac_sign>', views.get_info_by_number_zodiac_sign),
    path('<str:zodiac_sign>', views.get_info_by_zodiac_sign, name='horoscope_name')
]
