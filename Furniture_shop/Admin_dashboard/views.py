from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.db.models import Q
from . import forms


def user_admin(request):
    return render(request,'admin_home.html')

def user_admin_register(request):
    if request.session.has_key('admin_username'):
        return redirect('user_admin')
    else:
        if request.method=='POST':
            password=request.POST.get('password')
            confirm_password=request.POST.get('confirm_password')
            if password==confirm_password:
                firstname=request.POST.get('firstname')
                lastname=request.POST.get('lastname')
                username=request.POST.get('username')
                mobile_number=request.POST.get('mobile_number')
                email=request.POST.get('email')
                data=Admin_Member.objects.create(firstname=firstname,lastname=lastname,username=username,mobile_number=mobile_number,
                                         email=email,password=password,confirm_password=confirm_password)
                if data:
                    messages.success(request,'User profile created successfully!')
                    return redirect('user_admin_login')
                else:
                    messages.error(request,'Password does not match')
    return render(request,'admin_register.html')

def user_admin_login(request):
     if request.session.has_key('admin_username'):
        return redirect('user_admin')
     else:
        if request.method=='POST':
            username=request.POST.get('username_or_email')
            email=request.POST.get('username_or_email')
            password=request.POST.get('password')
            data_record=Admin_Member.objects.filter((Q(username=username)|Q(email=email)),password=password)
            if data_record.exists():
                user=data_record.first()
                request.session['admin_username']=user.username
                request.session['user_id']=user.id
                return redirect('user_admin')
            else:
                messages.error(request,'Invalid Username or Password')
        return render(request,'admin_login.html')
     
def user_admin_logout(request):
    if 'admin_username' in request.session:
        del request.session['admin_username']
        messages.success(request,'User logout successfully!')
    return redirect('user_admin_login')

# def admin_post(request):
#     if request.method=='POST':
#        product_name=request.POST.get('product_name')
#        product_price=request.POST.get('product_price')
#        product_size=request.POST.get('product_size')
#        product_image1=request.FILES['product_image1']
#        product_image2=request.FILES['product_image2']
#        product_image3=request.FILES['product_image3']
#        product_image4=request.FILES['product_image4']
#        product_image5=request.FILES['product_image5']
#        product_description= request.POST.get('product_description')
#        bed_material_subtype=request.POST.get('bed_material_subtype')
#        bed_text=request.POST.get('bed_text')
#        storage_type=request.POST.get('storage_type')
#        delivery_condition=request.POST.get('delivery_condition')
#        warranty=request.POST.get('warranty')
#        seller_name=request.POST.get('seller_name')
#        model_number=request.POST.get('model_number')
#        model_series=request.POST.get('model_series')
#        primary_color=request.POST.get('primary_color')
#        suitable_for=request.POST.get('suitable_for')
#        storage_included=request.POST.get('storage_included')
#        with_mattress=request.POST.get('with_mattress')
#        recommended_mattress_length=request.POST.get('recommended_mattress_length')
#        recommended_mattress_breadth=request.POST.get('recommended_mattress_breadth')
#        width=request.POST.get('width')
#        height=request.POST.get('height')
#        depth=request.POST.get('depth')
#        floor_clearance=request.POST.get('floor_clearance')
#        weight=request.POST.get('weight')
#        user_id=request.session['user_id']
#        u_id=Admin_Member.objects.get(id=int(user_id))
#        product=Product.objects.create(user_id=u_id,product_name=product_name,product_price=product_price,product_size=product_size,product_image1=product_image1,
#                                       product_image2=product_image2,product_image3=product_image3,product_image4=product_image4,
#                                       product_image5=product_image5,product_description=product_description,bed_material_subtype=bed_material_subtype,
#                                       bed_text=bed_text,storage_type=storage_type,delivery_condition=delivery_condition,
#                                       warranty=warranty,seller_name=seller_name,model_number=model_number,
#                                       model_series=model_series, primary_color=primary_color, suitable_for=suitable_for,
#                                       storage_included=storage_included,with_mattress=with_mattress,
#                                       recommended_mattress_length=recommended_mattress_length,recommended_mattress_breadth=recommended_mattress_breadth,
#                                       width=width,height=height,depth=depth,floor_clearance=floor_clearance,weight=weight)
#        if product:
#            messages.success(request,'Post Created Successfully!')
        
#     return render(request,'admin_post.html')
def admin_post(request,category):
    user_id = request.session['user_id']
    u_id = Admin_Member.objects.get(id=int(user_id))
    form = None
    if category == 'Bed':
        if request.method=='POST':
            form=forms.Bedform(request.POST,request.FILES)
            if form.is_valid():
                post=form.save(commit=False)
                post.user_id = u_id
                post.save()
                messages.success(request,'Post Created Successfully!')
                return redirect('user_admin')
        else:
            form=forms.Bedform()
    elif category == 'Gaming_Chair':
        if request.method=='POST':
            form=forms.GammingChairform(request.POST,request.FILES)
            if form.is_valid():
                post=form.save(commit=False)
                post.user_id = u_id
                post.save()
                messages.success(request,'Post Created Successfully!')
                return redirect('user_admin')
        else:
            form=forms.GammingChairform()
    return render(request,'admin_post.html',{'form':form})


def admin_post_name(request, category):
    user_id = request.session['user_id']
    u_id = Admin_Member.objects.get(id=int(user_id))
    Bed = Product.objects.filter(user_id=u_id) 
    gaming_chairs = Gaming_chair.objects.filter(user_id=u_id)
    if category == 'Bed':
        context = {'Bed': Bed}
    elif category == 'Gaming_Chair':
        context = {'gaming_chairs': gaming_chairs}
    return render(request, 'admin_post_name.html', context)


def admin_post_details(request,id,category):
    if category == 'Bed':
        post=Product.objects.get(id=id)
        form = forms.Bedform(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Details updated successfully!.")
            return redirect('user_admin')
    elif category == 'Gaming_Chair':
        post=Gaming_chair.objects.get(id=id)
        form = forms.GammingChairform(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Details updated successfully!.")
            return redirect('user_admin')
    
    return render(request,'admin_post_details.html',{'form':form})

def admin_post_delete(request,id,category):
    if category == 'Bed':
        Bed=Product.objects.get(id=id)
        context = {'Bed': Bed}
        if request.method=='POST':
            Bed.delete()
            messages.success(request, "Post Deleted Successfully!.")
            return redirect('user_admin')
    elif category == 'Gaming_Chair':
        gamming_chair=Gaming_chair.objects.get(id=id)
        context = {'gamming_chair': gamming_chair}
        if request.method=='POST':
            gamming_chair.delete()
            messages.success(request, "Post Deleted Successfully!.")
            return redirect('user_admin')
        
    return render(request,'admin_post_details.html',context)
    



       
           
           
   



def admin_profile(request,id):
    user=Admin_Member.objects.get(id=id)
    context={
        'user':user
    }
    if request.method=='POST':
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password==confirm_password:
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            username=request.POST.get('username')
            mobile_number=request.POST.get('mobile_number')
            email=request.POST.get('email')
            data=Admin_Member.objects.filter(id=id).update(firstname=firstname,lastname=lastname,username=username,mobile_number=mobile_number,
                                    email=email,password=password,confirm_password=confirm_password)
            if data:
                messages.success(request,'User Profile Updated successfully!')
                return redirect('user_admin')
    return render(request,'admin_profile.html',context)


