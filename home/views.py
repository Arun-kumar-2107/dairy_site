from django.shortcuts import render
from django.http import request,response,HttpResponse
def start(request):
    context={'page':'home page'}
    return render(request,'index.html',context )
# home page views
def Home(request):
    context={'page':'home page'}
    return render (request,'index.html',context)
# account page views
def account(request):
    context={'page':'account page'}

    return render (request,'account.html',context)
#product page views
def product(request):
    context={'page':'product page'}

    return render (request,'product.html',context)
# login page views
def login(request):
    context={'page':'login page'}

    return render (request,'login.html',context)
