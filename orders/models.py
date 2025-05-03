
from django.db import models
from users.models import User
from menu.models import Dish

ORDER_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('preparing', 'Preparing'),
    ('ready', 'Ready'),
    ('cancelled', 'Cancelled'),
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity}x {self.dish.name}"

    def total_price(self):
        return self.dish.price * self.quantity