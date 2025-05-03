from django.urls import path
from . import views  # Импортируем views

urlpatterns = [
    path('', views.menu_page, name='dish-list'),  # Изменили на функцию
]
