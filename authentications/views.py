from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import AdminUser
from helpers.decorators import auth_user_should_not_access
from django.contrib.auth.decorators import login_required

# Create your views here.
@auth_user_should_not_access
def registration(request):
    if request.method == 'POST':
        context = {'has_error':False, 'data':request.POST}
        username = request.POST.get('username')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm')
        
        #checking password length
        if len(password)<6:
            messages.add_message(request, messages.ERROR, 'Password Should Be atleast 6 Characters')
            context['has_error'] = True
           
        #checking if password match 
        if password != confirm_password:
            messages.add_message(request, messages.ERROR, "Password doesn't match!!")
            context['has_error'] = True
            
        #checking username
        if AdminUser.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, 'Username Already Taken')
            context['has_error'] = True
        
        #checking email
        if AdminUser.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, 'Email Already Taken')
            context['has_error'] = True
        
        #Save User
        user = AdminUser.objects.create_user(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = password
        )

        user.save()
        
        messages.add_message(request, messages.SUCCESS, 'Account Successfully Created you may login!')
        return redirect('login')
    return render(request, 'authentications/register.html')

#login user 
@auth_user_should_not_access
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Account Successfully Created you may login!')
            return redirect('dashboard')
        else:
            return render(request, 'main/login.html', {
                'message': "You don't have an account, Please register yourself"
            })
    return render(request, 'authentications/login.html' )

@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_image = request.FILES.get('profile')
        request.user.profile = profile_image
        request.user.save()
        return redirect('dashboard')

    return render(request, 'authentications/update_profile.html')

def logout_User(request):
  logout(request)
  return redirect(reverse('login'))