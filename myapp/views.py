from django import forms

from django.shortcuts import redirect, render,HttpResponse,HttpResponseRedirect,reverse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
#from django.contrib.auth import AuthenticationForm

# Create your views here.
from.models import *
from .forms import CreaterUserForm

def index(request):
 
    return render(request,('index.html'))
def course(request):
  return render(request,('course.html'))
def singlecourse(request):
    return render(request,('course-single.html'))
def category(request):
    return render(request,('category.html'))
def profile(request):
    if request.user.is_authenticated:
        return render(request,('profile.html'),{'name':request.user
    })   
    else:
        return render(request,('login.html'))

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username )
        print(password)

        # user=authenticate(request, username=username, password=password)
        user=User.objects.get(username=username)
        print('user authenticated')
        print(user)
        if user:
            login(request, user)
            messages.success(request,"Logged in successfully")
            print("login successfully")
            # return render(request,('index.html'))
            return HttpResponseRedirect(reverse('myapp:profile'))
        else:
            messages.info(request, 'Username or password is incorrect')
            print("not successful")
            

    
    return render(request,'login.html')
def about(request):
    # if request.method=="POST":
           
    #     name=request.POST.get('name')
    #     email=request.POST.get('email')
    #     phone=request.POST.get('phone')
    #     problem=request.POST.get('problem')
    #     about=Contact(name=name,email=email,phone=phone,problem=problem,date=datetime.today())
    #     about.save()
    #     messages.success(request,"Your message  has been sent successfully")

       # return HttpResponseRedirect(reverse('myapp:contact'))

    return render(request,('about.html')) 
    # return render(request,('about.html'))
def search(request):
    return HttpResponse('This is search page')
def logout_view(request):
    
    
    
    logout(request)
                             
     
    return render(request,'index.html') 
def lecturer(request):
    return render(request,('lecturer.html'))

def registration(request):
    form = CreaterUserForm()
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1==pass2:
           
            user_obj =User.objects.create(username=username,email=email,password=pass1)
            print(user_obj)
            
            return HttpResponseRedirect(reverse('myapp:login_view'))
            
            
        else:
            messages.error(request,"password does not match")
            print("password does not match")
            context = {
             'form': form
            }
            return render(request, 'registration.html', context)
           
       
       



        

    context = {
        'form': form
    }
    return render(request, 'registration.html', context)
    
    


def contact(request): 

    
    if request.method=="POST":
       
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        problem=request.POST.get('problem')
        contact=Contact(name=name,email=email,phone=phone,problem=problem,date=datetime.today())
        contact.save()
        messages.success(request,"Your message  has been sent successfully")

       # return HttpResponseRedirect(reverse('myapp:contact'))

    return render(request,('contact.html')) 
    

