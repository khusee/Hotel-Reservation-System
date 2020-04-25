from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is taken')
                redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email is already taken')
                    redirect('register')
                else:

                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    messages.success(request,'You are successfully registered')
                    return redirect('login')
        else:
            messages.error(request,'Password doesnt match')
            redirect('register')
    return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are logged in')
            return redirect('index')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('index')

