from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Article, Comment
from .forms import CommentForm
# Create your views here.


def articles_list(request):
    articles = Article.published.all()
    context = {'articles': articles}
    return render(request, 'blog/articles_list.html', context)


def article_detail(request, year, month, day, slug):
    article_details = get_object_or_404(Article, publish__year=year, publish__month=month, publish__day=day, slug=slug)
    comments = article_details.comments.filter(status='activado')
    # list of similar news
    news_tags_id = article_details.tags.values_list('id', flat=True)
    similar_article = Article.objects.filter(tags__in=news_tags_id).exclude(id=article_details.id)
    similar_article = similar_article.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:3]
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article_details
            new_comment.author = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {'article_details': article_details, 'comments': comments,
               'comment_form': comment_form, 'similar_article': similar_article}
    return render(request, 'blog/article_details.html', context)
