from django.urls import path
from .views import index, do_test

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('test/', do_test, name='test')
]
