from django.shortcuts import render


def do_test(request):
    return render(request, '404.html')


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def index(request):
    return render(request, 'index.html')
