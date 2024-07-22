from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from Admin_dashboard.models import *
from django.contrib import messages
from django.db.models import Q
import re
from django.db import IntegrityError
def home_page(request):
    return render(request,'home.html')

def user_register(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        gender=request.POST.get('gender')
        mobile_number=request.POST.get('mobile_number')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        # Validate phone number format
        phone_pattern = re.compile(r'^\d{10}$')
        if not phone_pattern.match(mobile_number):
            messages.error(request, "Please enter a valid phone number")
            return render(request, 'register.html')
        
        # Validate email format
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not email_pattern.match(email):
            messages.error(request, "Please enter a valid email address")
            return render(request, 'register.html')
        try:
            data=Member.objects.create(firstname=firstname,lastname=lastname,gender=gender,mobile_number=mobile_number,
                                    email=email,username=username,password=password)
            if data:
                    messages.success(request,'User Profile Created Successfully')

        except IntegrityError:
            messages.error(request,'Username or Email already exists')
    return render(request,'register.html')


def user_login(request):
    if request.session.has_key('username'):
        return redirect('user_dashboard')
    else:
        if request.method=='POST':
            username=request.POST.get('username_or_email')
            email=request.POST.get('username_or_email')
            password=request.POST.get('password')
            

            data_record=Member.objects.filter((Q(username=username)|Q(email=email)),password=password) 
            if data_record.exists():
                user = data_record.first()
                request.session['username']=user.username
                request.session['user_id']=user.id
                messages.success(request,'your login successfully!')
                return redirect('user_dashboard')
            else:
                messages.error(request,'Invalid Username/Email or Password')
    return render(request,'login.html')

def user_dashboard(request):
    return render(request,'home.html')  

def user_logout(request):
    if 'username' in request.session:
        del request.session['username']
        messages.success(request,'User logout successfully!')
    return redirect('user_login')          
          
def contact_page(request):
    return render(request,'contact.html')
def about_page(request):
    return render(request,'about.html')





def category(request,category):
    
    data=Product.objects.filter(Category_name=category)
    
    context={
        'data':data,
        
    }
    return render(request,'category.html',context)

def product(request,category,id):
    data=Product.objects.filter(Category_name=category).get(id=id)
    context={
        'data':data
    }
    return render(request,'product.html',context)



def user_profile(request):
    if request.session.has_key('username'):
        user_id = request.session['user_id']
        user=Member.objects.get(id=int(user_id))
    context={
        'user':user
    }
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        gender=request.POST.get('gender')
        mobile_number=request.POST.get('mobile_number')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        data=Member.objects.filter(id=user_id).update(firstname=firstname,lastname=lastname,gender=gender,username=username,mobile_number=mobile_number,
                                email=email,password=password)
        if data:
            messages.success(request,'User Profile Updated successfully!')
            return redirect('user_profile')
    
    return render(request,'dashboard.html',context)

def user_edit(request):
    return render(request,'dashboard.html')
from django.db.models import F
from django.db.models import Sum

def order_page(request):
    if request.session.has_key('username'):
        user_id = request.session['user_id']
        cart_items = Order.objects.filter(user=user_id)
        total_price = cart_items.aggregate(total_price=Sum('cart_price'))['total_price'] or 0
                
        context = {
            'cart_items': cart_items,
            'total_price': total_price,
        }
        return render(request, 'order.html', context)
    else:
        return redirect('user_login')
    
def remove_from_order(request, item_id):
    if request.session.has_key('username'):
        cart_item = Order.objects.get(id=item_id)
        cart_item.delete()
        return redirect('order_page')
    else:
        return redirect('user_login')

def cart_page(request):
    if request.session.has_key('username'):
        user_id = request.session['user_id']
        cart_items = Cart.objects.filter(user=int(user_id))
        total_price = cart_items.aggregate(total_price=Sum(F('cart_price')))['total_price'] or 0
                
        context = {
            'cart_items': cart_items,
            'total_price': total_price,
        }
        return render(request, 'cart.html', context)
    else:
        return redirect('user_login')

def add_to_cart(request, product_id):
    if 'username' in request.session:
        user_id = request.session['user_id']
        user = Member.objects.get(id=user_id)
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return HttpResponse("Product does not exist")

        Cart.objects.create(user=user, Product=product, quantity=1, cart_price=product.product_price)
        
        return redirect('cart_page')
    else:
        return redirect('user_login')

def remove_from_cart(request, item_id):
    if request.session.has_key('username'):
        cart_item = Cart.objects.get(id=item_id)
        cart_item.delete()
        return redirect('cart_page')
    else:
        return redirect('user_login')


from django.db.models import F

def update_cart(request, item_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        if quantity:
            try:
                quantity = int(quantity)
                cart_item = Cart.objects.get(id=item_id)
                product_price = cart_item.Product.product_price
                cart_item.quantity = quantity
                cart_item.cart_price = product_price * quantity
                cart_item.save()
            except (Cart.DoesNotExist, ValueError):
                # Handle exceptions if item not found or quantity is not valid
                pass
    return redirect('cart_page')
    




from django.contrib import messages
from django.db.models import Sum
from .models import Member, Product, Cart, Checkout, Order

from django.db import transaction



@transaction.atomic
def checkout(request):
    user_id = request.session.get('user_id')
    if not user_id:
        # Handle the case where user_id is not present in the session
        return redirect('login')  # Redirect to the login page or handle it appropriately

    # Retrieve the user's cart items
    cart_items = Cart.objects.filter(user_id=user_id)

    # If the cart is empty, redirect back to the cart page or display a message
    if not cart_items.exists():
        messages.error(request, 'Your cart is empty.')
        return redirect('cart_page')

    total_price = sum(cart_item.cart_price for cart_item in cart_items)

    if request.method == 'POST':
        # Retrieve checkout form data
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        country = request.POST.get('country')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        payment = 'Cash on delivery'

        with transaction.atomic():
            # Create a checkout instance
            checkout_instance = Checkout.objects.create(
                firstname=firstname,
                lastname=lastname,
                country=country,
                street=street,
                city=city,
                state=state,
                zipcode=zipcode,
                phone=phone,
                email=email,
                payment=payment
            )

            # Create orders for each item in the cart
            for cart_item in cart_items:
                order = Order.objects.create(
                    user_id=user_id,
                    Product=cart_item.Product,
                    quantity=cart_item.quantity,
                    cart_price=cart_item.cart_price,
                    status='Pending'
                )
                checkout_instance.carts.add(order)

            # Delete cart items after checkout
            cart_items.delete()

        messages.success(request, 'Your order has been placed successfully!')
        return redirect('home_page')

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'checkout.html', context)

def admin_page(request):
    return render(request,'home.html')

