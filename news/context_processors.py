from .models import Category


# context processor used to get all categories will be part of the menu base.html

def category(request):
    categories_link = Category.objects.all().filter(is_menu=True)
    return {'categories_link': categories_link}
