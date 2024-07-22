"""
home_page URL 
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('admin/',views.admin_page,name='admin_page'),
    path('register/',views.user_register,name='user_register'),
    path('login/',views.user_login,name='user_login'),
    path('user-logedin/',views.user_dashboard,name='user_dashboard'),
    path('logout/',views.user_logout,name='user_logout'),
    
    path('Category/<str:category>/',views.category,name='category'),
    path('Category/<str:category>/<int:id>/',views.product,name='product'),
    
    
    path('dashboard/',views.user_profile,name='user_profile'),
    path('dashboard/edit/',views.user_edit,name='user_edit'),
    path('order/',views.order_page,name='order_page'),
    path('cart/',views.cart_page,name='cart_page'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('delete/<int:item_id>/',views.remove_from_order,name='remove_from_order'),
    path('update_cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('contact-page/',views.contact_page,name='contact_page'),
    path('about-page/',views.about_page,name='about_page'),
    path('checkout/',views.checkout,name='checkout')
    
    
]
