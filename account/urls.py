from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('user/dashboard/save-news/', views.dashboard, name='dashboard'),
    # path('remove/<int:id>', views.remove_news, name='remove_news'),
    path('user/dashboard/edit/profile/', views.edit_profile, name='edit_profile'),
    path('register', views.register_user, name='register'),
    path('logout', views.logout_user, name='logout'),
    # path('remove/news/<int:id_news>', views.delete_user_news, name='remove-news'),


]
