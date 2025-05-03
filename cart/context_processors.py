from .models import CartItem

from django.db.models import Sum

def cart_item_count(request):
    if request.user.is_authenticated:
        count = CartItem.objects.filter(user=request.user).aggregate(total=Sum('quantity'))['total'] or 0
        return {'cart_item_count': min(count, 99)}
    return {'cart_item_count': 0}
