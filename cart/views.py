from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem
from menu.models import Dish

@login_required
def cart_page(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required
def cart_add(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    quantity = int(request.POST.get('quantity', 1))  # <-- добавь эту строку
    item, created = CartItem.objects.get_or_create(user=request.user, dish=dish)
    if not created:
        item.quantity += quantity
    else:
        item.quantity = quantity
    item.save()
    return redirect('menu-page')


@login_required
def cart_remove(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart-page')