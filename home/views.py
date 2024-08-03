from django.shortcuts import render,redirect
from django.http import request,response,HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# main code is here

#starting page
def start(request):
    context={'page':'home page'}
    return render(request,'index.html',context )
# home page views
@login_required(login_url='/login/')

def Home(request):
    context={'page':'home page'}
    return render (request,'index.html',context)
# account page views
@login_required(login_url='/login/')
def account(request):
    context={'page':'account page'}

    return render (request,'account.html',context)
#product page views
@login_required(login_url='/login/')
def product(request):
    context={'page':'product page'}

    return render (request,'product.html',context)
# login page views

def log_in(request):
    context = {'page': 'login page'}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/home/')

    return render(request, 'login.html', context)
# logout page views
def log_out(request):
    logout(request)
    return redirect ('/login/')

# register page views
def register(request):
    context = {'page': 'Registration'}
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken')
            return redirect('/register/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.info(request, 'Account created successfully')
        return redirect('/login/')

    return render(request, 'register.html', context)