from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!')


def about(request):
    return HttpResponse('А это вторая страница')
