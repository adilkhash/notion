from django.conf import settings


def generic(request):
    return {
        'DEBUG': settings.DEBUG,
    }
