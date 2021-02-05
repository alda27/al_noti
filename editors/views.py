from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article
from blog.forms import ArticleForm
# Create your views here.


def dashboard(request):
    if request.user.has_perm('blog.add_article'):
        articles = Article.objects.all().filter(author=request.user)
        context = {'articles': articles}
        return render(request, 'editors/dashboard.html', context)
    else:
        return redirect('home:home')




