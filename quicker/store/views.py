from django.views.generic import ListView, CreateView, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Product, Cart
from .forms import LoginForm

def home(request):
    return render(request, 'store/home.html')

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'store/register.html'
    success_url = reverse_lazy('login')  # Redirect to the login page after successful registration

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'store/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')  # Redirect to the dashboard page after successful login
            else:
                form.add_error(None, 'Invalid username or password')
        return render(request, 'store/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')

def dashboard(request):
    return render(request, 'store/dashboard.html')  # Make sure you have a dashboard template in the 'store' folder


def supermarkets(request):
    # Logic to display supermarket options or products
    return render(request, 'store/supermarkets.html')

def banks(request):
    # Logic to display banking options or products
    return render(request, 'store/banks.html')

def government(request):
    # Logic to display government services or information
    return render(request, 'store/government.html')

class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'

class AddToCartView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('cart')
