from django.urls import path
from . import views

urlpatterns = [
    path('', views.guest_user_index, name='index'),
    path('about', views.guest_user_about, name='about'),
    path('suvey', views.guest_user_survey, name='survey'),
]