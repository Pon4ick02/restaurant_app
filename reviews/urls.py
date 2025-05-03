from django.urls import path
from . import views  # Импортируем views

urlpatterns = [
    path('create/', views.reviews_page, name='review-create'),  # Изменили на функцию
    path('delete/<int:review_id>/', views.review_delete_html, name='review-delete'),  # Изменили на функцию
]
