from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.db.models import Count
from .models import Article, Comment
from .forms import CommentForm, ArticleForm


# Create your views here.


def articles_list(request):
    articles = Article.published.all()
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    page_list_article = paginator.get_page(page_number)
    context = {'articles': page_list_article}
    return render(request, 'blog/articles_list.html', context)


def article_detail(request, year, month, day, slug):
    article_details = get_object_or_404(Article, publish__year=year, publish__month=month, publish__day=day, slug=slug)
    # comments = article_details.comments.filter(status='activado')
    # list of similar news
    news_tags_id = article_details.tags.values_list('id', flat=True)
    similar_article = Article.objects.filter(tags__in=news_tags_id).exclude(id=article_details.id)
    similar_article = similar_article.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:3]
    # TODO: hacer el listado de los posts destacados
    # if request.method == 'POST':
    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         new_comment = comment_form.save(commit=False)
    #         new_comment.article = article_details
    #         new_comment.author = request.user
    #         new_comment.save()
    # else:
    #     comment_form = CommentForm()

    context = {'article_details': article_details,
               # 'comments': comments,
               # 'comment_form': comment_form,
               'similar_article': similar_article}

    return render(request, 'blog/article_details.html', context)


@login_required()
def edit_article(request, article_id):
    article = get_object_or_404(Article, author=request.user, id=article_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form_modified = form.save(commit=False)
            form_modified.slug = '-'.join(form.cleaned_data['title'].split()).lower()
            # form_modified.tags = form.cleaned_data['tags']
            # form_modified.author = request.user
            if 'photo' in request.FILES:
                form_modified.photo = request.FILES['photo']
            form_modified.save()
            return redirect('editors:dashboard')
    else:
        form = ArticleForm(instance=article)
    context = {'article': article, 'form': form}

    return render(request, 'blog/edit_article.html', context)


class DeleteArticleView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('editors:dashboard')
    template_name = 'blog/article_confirm_delete.html'
