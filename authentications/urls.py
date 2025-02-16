from django.urls import path
from . import views

urlpatterns = [
  path('', views.login_user, name='login'),
  path('register', views.registration, name='register'),
  path('logout', views.logout_User, name='logout'),
  path('EditProfile/', views.update_profile, name='update_user_profile'),
  path('dashboard', views.dashboard_views, name='dashboard'),
  path('charts', views.chart_view, name='charts'),
  path('tables', views.table_view, name='tables'),
]