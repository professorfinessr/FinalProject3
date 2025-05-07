from django.shortcuts import render, redirect
from .models import FoodItem, Order
# from .forms import CustomerForm

# Create your views here.

def menu_view(request):
    items = FoodItem.objects.all()
    return render(request, 'FoodTruck/menu.html', {'items': items})

def cart_view(request):
    cart = request.session.get('cart', [])
    items = FoodItem.objects.filter(id__in=cart)
    total = sum(item.price for item in items)
    return render(request, 'FoodTruck/cart.html', {'items': items, 'total': total})

def add_to_cart(request, item_id):
    cart = request.session.get('cart', [])
    cart.append(item_id)
    request.session['cart'] = cart
    return redirect('menu')

"""def checkout_view(request):
    cart = request.session.get('cart', [])
    items = FoodItem.objects.filter(id__in=cart)

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            order = Order.objects.create(customer=customer)
            order.items.set(items)
            order.save()
            request.session['cart'] = [] # clears cart
            return render(request, 'FoodTruck/thank_you.html', {'order': order})
        else:
            form = CustomerForm()

        return render(request, 'FoodTruck/checkout.html', {'form': form, 'items': items})
        """