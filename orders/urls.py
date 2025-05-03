from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders_page, name='orders-page'),
    path('create/', views.order_create_html, name='order-create'),
    path('<int:order_id>/update/', views.update_order_status, name='order-update'),
    path('<int:order_id>/delete/', views.delete_order, name='order-delete'),
    path('history/user/', views.order_history_user, name='order_history_user'),
    path('history/seller/', views.order_history_seller, name='order_history_seller'),
]
