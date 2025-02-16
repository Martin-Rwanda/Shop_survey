from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import AdminUser
from helpers.decorators import auth_user_should_not_access
from django.contrib.auth.decorators import login_required

# Create your views here.
def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm')

        #checking password 
        if password != confirm_password:
            return render(request, 'main/register.html', {
                'message': "Password doesn't match!!"
            })
        
        #checking username 
        if AdminUser.objects.filter(username=username).exists():
            return render(request, 'main/register.html', {
                'message': "User Name already exist..!!"
            })
        
        #Save User

        user = AdminUser.objects.create_user(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = password
        )

        user.save()
        return redirect('login')
    return render(request, 'main/register.html')