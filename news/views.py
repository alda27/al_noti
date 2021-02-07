from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.db.models import Count
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.views.generic import DeleteView

from .forms import SearchForm, CreateNewForm
from .models import News


def news_list(request, category, id):
    list_news = News.published.all().filter(category__name__iexact=category, category__id=id).order_by('-publish')
    paginator = Paginator(list_news, 9)
    page_number = request.GET.get('page')
    page_list_news = paginator.get_page(page_number)
    context = {
        'list_news': page_list_news
    }
    return render(request, 'news/list_news.html', context)


# podemos crear una vista como la de arriba pero que envie el context al template base para usarlo en la barra
# de navegacion edit: no pude :(, tuve que crear un context processor para hacerla global y obtener las categorias


def news_detail(request, category, year, month, day, slug):
    news_detail = get_object_or_404(News, publish__year=year, publish__month=month, publish__day=day, slug=slug,
                                    category__name=category)
    popular_news = News.published.filter(is_popular=True)[:6]
    # list of similar news
    news_tags_id = news_detail.tags.values_list('id', flat=True)
    similar_news = News.published.filter(tags__in=news_tags_id).exclude(id=news_detail.id)
    similar_news = similar_news.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:3]
    context = {'news_detail': news_detail,
               'popular_news': popular_news,
               'similar_news': similar_news}
    return render(request, 'news/news_detail.html', context)

@login_required()
def create_news(request):
    if request.method == 'POST':
        form = CreateNewForm(request.POST, request.FILES)
        if form.is_valid():
            news_form = form.save(commit=False)
            news_form.author = request.user
            news_form.slug = '-'.join(form.cleaned_data['title'].split()).lower()
            if 'photo' in request.FILES:
                news_form.photo = request.FILES['photo']
            news_form.save()
            form.save_m2m()
            return redirect('account:dashboard')
    else:
        form = CreateNewForm()
    context = {'form': form}
    return render(request, 'news/create_news.html', context)


@login_required
@require_POST
def news_save(request):
    news_id = request.POST.get('id')
    action = request.POST.get('action')
    if news_id and action:
        try:
            news = News.objects.get(id=news_id)
            if action == 'save':
                news.user_save.add(request.user)
                news.date_user_save = datetime.now()
                news.save()
            else:
                news.user_save.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'ko'})


def search_news(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', 'body')
            search_query = SearchQuery(query)
            results = News.objects.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(search=search_query).order_by('-rank')
    context = {'form': form, 'query': query, 'results': results}
    return render(request, 'news/search.html', context)


@login_required()
def edit_news(request, news_id):
    news = get_object_or_404(News, author=request.user, id=news_id)

    if request.method == 'POST':
        form = CreateNewForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form_modified = form.save(commit=False)
            form_modified.slug = '-'.join(form.cleaned_data['title'].split()).lower()
            # form_modified.tags = form.cleaned_data['tags']
            # form_modified.author = request.user
            if 'photo' in request.FILES:
                form_modified.photo = request.FILES['photo']
            form_modified.save()
            form.save_m2m()
            return redirect('account:dashboard_news')
    else:
        form = CreateNewForm(instance=news)
    context = {'news': news, 'form': form}

    return render(request, 'news/edit_news.html', context)


class DeleteNewsView(LoginRequiredMixin, DeleteView):
    model = News
    success_url = reverse_lazy('account:dashboard_news')
    template_name = 'news/news_confirm_delete.html'
