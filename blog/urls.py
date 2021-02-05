from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.article_detail, name='article_detail'),
    path('dashboard/edit/<int:article_id>/', views.edit_article, name='article_edit'),
    path('dashboard/delete/<int:pk>/', views.DeleteArticleView.as_view(), name='article_delete'),
]