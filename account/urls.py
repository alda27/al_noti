from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/save-news', views.dashboard_news, name='dashboard_news'),
    path('dashboard/articles', views.dashboard_article, name='dashboard_articles'),
    # path('remove/<int:id>', views.remove_news, name='remove_news'),
    path('dashboard/profile-edit', views.edit_profile, name='edit_profile'),
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('logout', views.logout_user, name='logout'),
    # path('remove/news/<int:id_news>', views.delete_user_news, name='remove-news'),


]
