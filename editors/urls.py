from django.urls import path
from . import views

app_name = 'editors'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/edit/<int:user_id>/', views.edit_article, name='edit_article'),
    #     path('save/', views.news_save, name='news_save')
]
