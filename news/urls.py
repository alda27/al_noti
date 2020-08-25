from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('<str:category>/', views.news_list, name='news_list'),
    path('<str:category>/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.news_detail, name='news_detail'),

]