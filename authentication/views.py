from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()


def index(request):
    return render(request,'index.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birthdate = request.POST.get('birthdate')

        try:
            user = User.objects.create_user(
                username=username, 
                password=password, 
                email=email, 
                first_name=first_name, 
                last_name=last_name, 
                birthdate=birthdate
            )
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('Login')
        except IntegrityError:  # Handle duplicate username or other integrity errors
            messages.error(request, 'Username or email already exists')
        except Exception as e:
            messages.error(request, f'Error: {e}')
    
    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        if '@' in username_or_email:
            try:
                user_obj = User.objects.get(email=username_or_email)
                username = user_obj.username
            except User.DoesNotExist:
                messages.error(request, 'Invalid email or password')
                return redirect('Login')
        else:
            username = username_or_email
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')  
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('Login') 
        
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('Login')

