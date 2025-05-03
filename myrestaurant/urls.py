from django.contrib import admin
from django.urls import path, include
from users.views import RegisterView, CustomLoginView, CustomLogoutView
from menu.views import menu_page
from cart.views import cart_page, cart_add, cart_remove
from orders.views import orders_page
from reviews.views import reviews_page, review_delete_html
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/menu/', include('menu.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/reviews/', include('reviews.urls')),
    # Frontend views
    path('', menu_page, name='menu-page'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('cart/', cart_page, name='cart-page'),
    path('cart/add/<int:dish_id>/', cart_add, name='cart-add'),
    path('cart/remove/<int:item_id>/', cart_remove, name='cart-remove'),
    path('orders/', orders_page, name='orders-page'),
    path('reviews/', reviews_page, name='reviews-page'),
    path('reviews/delete/<int:review_id>/', review_delete_html, name='review-delete-html'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)