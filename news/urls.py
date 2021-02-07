from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('<str:category>/<int:id>/', views.news_list, name='news_list'),
    path('<str:category>/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.news_detail, name='news_detail'),
    path('create/', views.create_news, name='create_news'),
    path('save/', views.news_save, name='news_save'),
    path('search/', views.search_news, name='search_news'),
]