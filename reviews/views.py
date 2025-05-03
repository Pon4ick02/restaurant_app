from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from menu.models import Dish
from orders.models import OrderItem

def reviews_page(request):
    # Все отзывы по убыванию даты
    reviews = Review.objects.all().order_by('-created_at')

    # Фильтрация по блюду
    filter_id = request.GET.get('filter_dish')
    if filter_id:
        reviews = reviews.filter(order_item__dish_id=filter_id)

    dishes = Dish.objects.filter(available=True)

    allowed_order_items = []
    if request.user.is_authenticated:
        past_items = OrderItem.objects.filter(order__user=request.user)
        # Только те, на которые ещё нет отзыва
        for item in past_items:
            if not Review.objects.filter(order_item=item).exists():
                allowed_order_items.append(item)

        if request.method == 'POST':
            order_item_id = request.POST.get('order_item')
            text = request.POST.get('text')
            stars = request.POST.get('stars')
            anonymous = 'anonymous' in request.POST

            try:
                order_item = OrderItem.objects.get(id=order_item_id, order__user=request.user)
            except OrderItem.DoesNotExist:
                return redirect('reviews-page')

            # Проверка: уже оставлен отзыв?
            if Review.objects.filter(order_item=order_item).exists():
                return redirect('reviews-page')

            Review.objects.create(
                user=None if anonymous else request.user,
                order_item=order_item,
                text=text,
                stars=stars,
                anonymous=anonymous
            )
            return redirect('reviews-page')

    return render(request, 'reviews.html', {
        'reviews': reviews,
        'dishes': dishes,
        'allowed_order_items': allowed_order_items,
    })


@login_required
def review_delete_html(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user == review.user or request.user.is_superuser:
        review.delete()
    return redirect('reviews-page')
