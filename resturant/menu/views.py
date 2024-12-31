from django.shortcuts import render,redirect
from menu.models import Menu

def home(request):
    return render(request,'home.html')

def add_menu(request):

    if request.method=="POST":
        n=request.POST['n']
        d=request.POST['d']
        p=request.POST['p']
        i=request.FILES['i']
        m=Menu.objects.create(name=n,description=d,price=p,image=i)
        m.save()

        # return view_menu(request)
        return redirect('menu:view')

    return render(request,'add.html')

def view_menu(request):
    k=Menu.objects.all()
    return render(request,'view.html',{'menu':k})

def details(request,m):
    k=Menu.objects.get(id=m)
    return render(request,'details.html',{'menu':k})

def edit(request,m):
    k=Menu.objects.get(id=m)
    if request.method == "POST":
        k.name=request.POST['n']
        k.description=request.POST['d']
        k.price=request.POST['p']


        if request.FILES.get('i')==None:
            k.save()
        else:
            k.image=request.FILES.get('i')
        k.save()
        return view_menu(request)
    return render(request,'edit.html',{'menu':k})


def delete(request,m):
    k=Menu.objects.get(id=m)
    k.delete()
    # return view_menu(request)
    return redirect('menu:view')

