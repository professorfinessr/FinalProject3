from django.shortcuts import render
from .models import FoodItem

# Create your views here.

def menu_view(request):
    return render(request, 'FoodTruck/menu.html', {})

def cart_view(request):
    cart = request.session.get('cart', [])
    items = FoodItem.objects.filter(id__in=cart)
    total = sum(item.price for item in items)
    return render(request, 'FoodTruck/cart.html', {'items': items, 'total': total})