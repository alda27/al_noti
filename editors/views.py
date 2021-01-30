from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article
from .forms import ArticleForm
# Create your views here.


def dashboard(request):
    if request.user.has_perm('blog.add_article'):
        articles = Article.objects.all().filter(author=request.user)
        context = {'articles': articles}
        return render(request, 'editors/dashboard.html', context)
    else:
        return redirect('home:home')


def edit_article(request, user_id):
    article = get_object_or_404(Article, author=request.user, id=user_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form_modified = form.save(commit=False)
            form_modified.slug = '-'.join(form.cleaned_data['title'].split())
            # form_modified.tags = form.cleaned_data['tags']
            form_modified.author = request.user
            if 'photo' in request.FILES:
                form_modified.photo = request.FILES['photo']
            form_modified.save()
    else:
        form = ArticleForm(instance=article)
    context = {'article': article, 'form': form}

    return render(request, 'editors/edit_article.html', context)