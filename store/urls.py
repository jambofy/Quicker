# store/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import home, RegisterView, LoginView, dashboard, supermarkets, banks, government, ProductListView, AddToCartView, logout

urlpatterns = [
    path('', home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('supermarkets/', supermarkets, name='supermarkets'),
    path('banks/', banks, name='banks'),
    path('government/', government, name='government'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('cart/add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    # Add other URL patterns as needed
]
