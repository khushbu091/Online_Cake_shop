from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def product(request):
    return render(request, 'product.html')
def contact(request):
    return render(request, 'contact.html')
def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')
def registerdata(request):
    firstname=request.POST.get('firstName')
    lastname=request.POST.get('lastName')
    email=request.POST.get('email')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')

    data=User.objects.filter(Email=email)
    print(data)

    if data:
        msg="email already exist"
        return render(request,'register.html',{'key':msg})
    else:
        if password==cpassword:
            User.objects.create(
                Firstname=firstname,
                Lastname=lastname,
                Email=email,
                Password=password,
            )
            msg='registeration'
            return render(request,'login.html',{'key':msg})
        else:
            msg='password and confirm password matched'
            return render(request,'register.html',{'key':msg})
        
def logindata(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    user=User.objects.filter(Email=email)
    if user:
        data=User.objects.get(Email=email)
        pss=data.Password
        if pss==password:
            context={
                'name':data.Firstname,
                'email':data.Email,
                'logout':'logout'
            }
            return render(request,'dashbord.html',{'context':context})
        else:
            msg="enter valid Email"
            return render(request,'login.html',{'key':msg})
    else:
        msg="Enter Valid Email"
        return render (request,'login.html',{'key':msg})

def dashbord(request):
    return render(request, 'dashbord.html')
def logout(request):
    return render(request, 'home.html')