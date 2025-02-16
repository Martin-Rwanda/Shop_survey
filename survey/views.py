from django.shortcuts import render, redirect
from .models import Product, SurveyResponse
from helpers.decorators import auth_user_should_not_access
from django.contrib import messages

# Create user views here.
@auth_user_should_not_access
def guest_user_index(request):
    return render(request, 'survey/index.html')
# Create about here.
@auth_user_should_not_access
def guest_user_about(request):
    return render(request, 'survey/about.html')
# Create home views here.
@auth_user_should_not_access
def guest_user_survey(request):
    return render(request, 'survey/survey.html')