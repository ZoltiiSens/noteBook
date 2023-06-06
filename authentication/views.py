from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


def home(request):
    return render(request, 'authentication/home.html')


def signup_user(request):
    context = {'form': UserCreationForm()}
    if request.method == 'GET':
        return render(request, 'authentication/signup.html', context)
    else:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                login(request, user)
                return redirect('week_list')
            except IntegrityError:
                context['error'] = 'Username has already been taken. Choose the other one'
                return render(request, 'authentication/signup.html', context)
        else:
            context['error'] = 'Passwords did not match. Try Again!'
            return render(request, 'authentication/signup.html', context)


def login_user(request):
    context = {'form': AuthenticationForm()}
    if request.method == 'GET':
        return render(request, 'authentication/login.html', context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('week_list')
        else:
            context['error'] = 'Password or username is wrong. Try Again!'
            return render(request, 'authentication/login.html', context)


@login_required
def logout_user(request):
    if request.method == 'GET':
        return redirect('home')
    else:
        logout(request)
        return redirect('home')
