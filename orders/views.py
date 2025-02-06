from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from products.models import Product
from django.http import HttpResponse

# Create your views here.

@login_required
def create_order(request):
    if request.method == 'POST':
        product_ids = request.POST.getlist('products')
        products = Product.objects.filter(id__in=product_ids)
        total_price = sum(product.price for product in products)

        order = Order.objects.create(user=request.user, total_price=total_price)
        for product in products:
            OrderItem.objects.create(order=order, product=product, quantity=1)

        return redirect('order_list')

    products = Product.objects.all()
    return render(request, 'orders/create_order.html', {'products': products})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def view_order(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/view_order.html', {'order': order})
