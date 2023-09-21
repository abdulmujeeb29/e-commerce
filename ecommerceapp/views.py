from django.shortcuts import render
from django.contrib import messages
from .models import CustomUser
from django.shortcuts import redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        username =request.POST['username']
        email =request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']
        

        if password1== password2:
            if CustomUser.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return render(request,'register.html')


            elif CustomUser.objects.filter(username=username).exists() :
                messages.info(request,'Username already used')
                return render(request,'register.html')

            elif len(username) >10 :
                messages.info(request,'username must be less than 10 characters ')

            elif not username.isalnum():
                messages.info(request,' Username should be Alphanumeric characters only ')

            else:
                user = CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                    
                )

                
                user=authenticate(email=email, password=password1)

                if user is not None:
                    auth.login(request,user)
                    return redirect('/')

        else:
            messages.info(request,"Passwords doesn't corresspond" )

    return render(request,'signup.html')

def signin(request):
    if request.method == "POST":

        email = request.POST['email']
        password1 = request.POST['password1']
        user = authenticate(email=email,password=password1)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Email or password')
    
    return render(request,'signin.html')