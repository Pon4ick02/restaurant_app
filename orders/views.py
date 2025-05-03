from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem, ORDER_STATUS_CHOICES
from cart.models import CartItem
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def orders_page(request):
    if request.user.is_seller:
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(user=request.user)

    for order in orders:
        total_price = 0
        for item in order.items.all():
            item.total_price = item.dish.price * item.quantity
            total_price += item.total_price
        order.total_price = total_price

    return render(request, 'orders.html', {
        'orders': orders,
        'status_choices': ORDER_STATUS_CHOICES  # 👈 Добавлено это
    })
@login_required
def order_create_html(request):
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user=request.user)
        if cart_items.exists():
            # Создаём заказ
            order = Order.objects.create(user=request.user)

            # Переносим блюда из корзины в заказ
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    dish=item.dish,
                    quantity=item.quantity
                )

            # Очищаем корзину
            cart_items.delete()

            return redirect('orders-page')
    return redirect('cart-page')  # если не POST или корзина пуста


@login_required
@require_POST
def update_order_status(request, order_id):
    if not request.user.is_seller:
        return HttpResponseForbidden()

    new_status = request.POST.get('status')
    try:
        order = Order.objects.get(id=order_id)
        order.status = new_status
        order.save()
    except Order.DoesNotExist:
        pass

    return redirect('orders-page')


@login_required
@require_POST
def delete_order(request, order_id):
    if not request.user.is_seller:
        return HttpResponseForbidden()

    try:
        order = Order.objects.get(id=order_id)
        order.delete()
    except Order.DoesNotExist:
        pass

    return redirect('orders-page')

@login_required
def order_history_user(request):
    orders = Order.objects.filter(user=request.user, is_archived=True)
    return render(request, 'orders/order_history_user.html', {'orders': orders})

@login_required
def order_history_seller(request):
    if not request.user.is_seller:
        return redirect('menu')  # или куда хочешь
    orders = Order.objects.filter(is_archived=True)  # все удалённые
    return render(request, 'orders/order_history_seller.html', {'orders': orders})