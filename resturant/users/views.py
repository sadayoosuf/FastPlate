from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

def register(request):
    if request.method =="POST":
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']

        if(p==cp):
            u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            u.save()
        else:
            return HttpResponse('invalid credential')
        return redirect('users:user_login')

    return render(request,'register.html')

def user_login(request):
    if request.method=="POST":
        u=request.POST['u']
        p=request.POST['p']

        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
        else:
            return HttpResponse("invalid user")
        return redirect('menu:home')
    return render(request,'login.html')

def user_logout(request):
    logout(request)

    return redirect('users:user_login')
