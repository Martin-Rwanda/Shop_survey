from django.urls import path
from . import views

urlpatterns = [
  path('', views.login_user, name='login'),
  path('register', views.registration, name='register'),
  path('logout', views.logout_User, name='logout'),
  path('EditProfile/', views.update_profile, name='update_user_profile'),
]