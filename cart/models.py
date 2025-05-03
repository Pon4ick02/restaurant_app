
from django.db import models
from users.models import User
from menu.models import Dish

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'dish')  # Один и тот же dish не может дублироваться в корзине

    def __str__(self):
        return f"{self.quantity}x {self.dish.name} ({self.user.username})"
