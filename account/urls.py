from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/edit', views.edit, name='edit_profile'),
    path('register', views.register_user, name='register'),
    path('logout', views.logout_user, name='logout'),

]
