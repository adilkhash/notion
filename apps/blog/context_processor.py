import sys
import django
from django.conf import settings


def generic(request):
    return {
        'DEBUG': settings.DEBUG,
        'DJANGO_VERSION': django.__version__,
        'PYTHON_VERSION': sys.version[:6]
    }
