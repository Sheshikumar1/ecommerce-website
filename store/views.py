from django.shortcuts import render,redirect
from . models import Product,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{'products':products})

def about(request):
    return render(request,'about.html',{})

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"logged in successfully")
            return redirect('home')
        else:
            messages.success(request,"There was an error logging in, please try again")
            return redirect('login')

    else:
        return render(request, 'login.html',{})
        



def logout_user(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')

def register(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')

            #log in user
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"Registration successful")
            return redirect('home')
        else:
            messages.error(request,"Registration failed, please try again")
            return redirect('register')
    else:
        return render(request,'register.html',{'form':form})
    
def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})
def category(request,foo):
    foo=foo.replace('-',' ')
    try:
        category=Category.objects.get(name=foo)
        products=Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products,'category':category})
    except:
        messages.error(request,"That categoty does not exist")         
        return redirect('home')
