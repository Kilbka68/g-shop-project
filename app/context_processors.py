from .models import Category


def category_context(request):
    return {
        'categories': Category.objects.filter(parent=None)
    }