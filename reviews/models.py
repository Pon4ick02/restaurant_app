from django.db import models
from django.contrib.auth import get_user_model
from orders.models import OrderItem

User = get_user_model()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    stars = models.PositiveIntegerField()
    anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def dish(self):
        return self.order_item.dish

    def __str__(self):
        return f"Review by {self.user or 'Anonymous'} on {self.dish.name}"
