from django.db import models
from django.db.models import Avg



class Dish(models.Model):
    CATEGORY_CHOICES = [
        ('cold', 'Cold Dishes'),
        ('hot', 'Hot Dishes'),
        ('dessert', 'Desserts'),
        ('drink', 'Drinks'),
    ]

    name        = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=8, decimal_places=2)
    weight      = models.PositiveIntegerField(help_text="Weight in grams")
    available = models.BooleanField(default=True)
    image       = models.ImageField(
                    upload_to='menu_images/',
                    blank=True,
                    null=True,
                    default='menu_images/default.jpg'
                  )
    category    = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='cold')

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        # Импортируем модель Review здесь, чтобы избежать циклической зависимости
        from reviews.models import Review

        # Ставки по звёздам всех отзывов, привязанных к этому блюду через OrderItem
        result = Review.objects.filter(order_item__dish=self) \
            .aggregate(avg_stars=Avg('stars'))
        avg = result['avg_stars']
        # Округляем до одного знака после запятой, либо 0, если отзывов нет
        return round(avg, 1) if avg is not None else 0