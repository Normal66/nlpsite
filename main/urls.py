from django.urls import path
from .views import index, do_test, trening_list, trening_detail

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('test/', do_test, name='test'),
    path('trening/', trening_list, name='product_list'),
    path('trening/<slug:category_slug>/', trening_list, name='product_list_by_category'),
    path('trening/<int:id>/<slug:slug>/', trening_detail, name='product_detail'),
]
