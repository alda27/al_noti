from .models import Category


def category(request):
    categories_link = Category.objects.all()
    return {'categories_link': categories_link}
