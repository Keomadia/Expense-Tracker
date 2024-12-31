from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
    if request.method =="POST":
        name = request.POST.get('fnm')
        passkey = request.POST.get('pwd')
        email = request.POST.get('emailid')
        user = User.objects.create_user(username=name, password=passkey, email = email)
        login(request,user.save())
        return redirect("home:home") 
    return render(request,'users/signup.html')


def login_view(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            if 'next' in request.POST: 
                return redirect(request.POST.get('next'))
            else:
                return redirect("home:home") 
        else:
            error = "Invalid Credentials"
            return  render(request, "users/login.html",{'error': error})
        
    return render(request,'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

