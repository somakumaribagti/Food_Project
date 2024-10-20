from django.shortcuts import render,redirect
from django.http import HttpResponse
from Home_App.models import Book_Table, ItemList ,Items
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def HomeView(request):
    items =  Items.objects.all()
    list = ItemList.objects.all()
    return render(request,'home.html',{'items': items, 'list': list})

def SingnUpView(request):
    if request.method == 'POST':
        username= request.POST.get("uname")
        email= request.POST.get('email')
        password= request.POST.get('password')
        confirmpassword= request.POST.get('confirmpassword')
        if password!=confirmpassword:
            return redirect("/")
        try:
            if User.object.get(username=username):
                return redirect("/")
        except:
            pass
        try:
            if User.object.get(email=email):
                return redirect("/")            
        except:
            pass
        query= User.objects.create_user(username,email,password)
        query.save()
    return render(request,"index.html")    
    


def SignInView(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        myuser=authenticate(username=uname,password=password)
        if myuser is not None:
            login(request,myuser)
            return redirect("/")
        else:
            return redirect("/index.html")       
    return render(request,'login.html')   

def AboutView(request):
    return render(request,'about.html')

def MenuView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request,'menu.html',{'items': items, 'list': list})

def BookTableView(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        number= request.POST.get('number')
        date= request.POST.get('date')
        person= request.POST.get('person')
        if name !='' and email !='' and number !='' and date !='' and person !=''  :
            data= Book_Table(Name=name,Email=email,Person=person,Date=date,Number=number)
            data.save()
    return render(request,'book_table.html')    
