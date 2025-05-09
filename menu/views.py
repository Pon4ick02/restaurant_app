from django.shortcuts import render
from .models import Dish

def menu_page(request):

    categories = Dish.CATEGORY_CHOICES
    selected = request.GET.get('category')

    if selected in dict(categories):
        dishes = Dish.objects.filter(category=selected)
    else:
        dishes = Dish.objects.all()
        selected = None

    return render(request, 'menu.html', {
        'dishes': dishes,
        'categories': categories,
        'selected_category': selected,
    })

