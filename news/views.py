from django.shortcuts import render, get_object_or_404, HttpResponse
from django.db.models import Count
import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import News


def news_list(request, category, id):
    list_news = News.published.all().filter(category__name__iexact=category, category__id=id).order_by('-publish')
    context = {
        'list_news': list_news
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
            else:
                news.user_save.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'ko'})


