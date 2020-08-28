from django.shortcuts import render
from news.models import News, Category
from blog.models import Article
# Create your views here.


def home(request):
    popular_news = News.published.filter(is_popular=True)[:6]
    last_news = News.published.order_by('-publish').first()
    latest_news = News.published.order_by('-publish')[:4]
    latest_articles = Article.objects.all().order_by('-publish')[:6]
    context = {
                'popular_news': popular_news,
                'last_news': last_news,
                'latest_news': latest_news,
                'latest_articles': latest_articles,

                }
    return render(request, 'home/home.html', context)



