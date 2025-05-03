from django.urls import path
from . import views  # Импортируем views

urlpatterns = [
    path('', views.cart_page, name='cart-list'),  # Изменили на функцию
    path('add/<int:dish_id>/', views.cart_add, name='cart-add'),  # Изменили на функцию
    path('delete/<int:item_id>/', views.cart_remove, name='cart-delete'),  # Изменили на функцию
]
