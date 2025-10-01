# menu/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MenuItem, Category, Order, OrderItem

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('menu_list')
    else:
        form = UserCreationForm()
    return render(request, 'menu/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('menu_list')
    else:
        form = AuthenticationForm()
    return render(request, 'menu/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('menu_list')

def menu_list(request):
    category_name = request.GET.get('category')
    
    # Filter items if a category is selected
    if category_name:
        items = MenuItem.objects.filter(category__name=category_name)
    else:
        items = MenuItem.objects.all()
    
    categories = Category.objects.all()
    return render(request, 'menu/menu_list.html', {'items': items, 'categories': categories})

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, menu_item=item)
    
    if not created:
        order_item.quantity += 1
        order_item.save()
        
    messages.success(request, f"'{item.name}' was added to your cart!")
    return redirect('menu_list')

@login_required
def view_cart(request):
    order = Order.objects.filter(user=request.user, is_ordered=False).first()
    return render(request, 'menu/cart.html', {'order': order})