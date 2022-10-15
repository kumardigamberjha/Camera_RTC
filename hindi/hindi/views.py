from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def LoginView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, 'Login Done')
        redirect('/')
    else:
        messages.error(request, 'Invalid Credentials')
    return render(request, 'welcome/login.html')

def LogoutView(request):
    logout(request)
    return redirect('login')