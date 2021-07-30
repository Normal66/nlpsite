from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import m_SprMenu, m_Category, m_Trening

def do_test(request):
    return render(request, '404.html')


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def index(request):
    return render(request, 'index.html')


def trening_list(request, category_slug=None):
    category = None
    categories = m_Category.published.all()
    products = m_Trening.published.all()
    if category_slug:
        category = get_object_or_404(m_Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main/list.html', {'category': category, 'categories': categories, 'products': products})


def trening_detail(request, id, slug):
    product = get_object_or_404(m_Trening, id=id, slug=slug, cansw=True)
    return render(request, 'main/detail.html', {'product': product})
