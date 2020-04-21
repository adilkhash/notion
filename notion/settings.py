import os

from django.utils.translation import ugettext_lazy as _
import environ

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()
root = environ.Path(__file__) - 2

BASE_DIR = str(root)

SECRET_KEY = env.str('SECRET_KEY', 'my-santa-claus')

DEBUG = env.bool('DEBUG', True)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.redirects',
    'django.contrib.sitemaps',

    # project apps
    'apps.blog',
    'apps.notes',

    # 3rd party apps
    'redactor',
    'bootstrap_pagination',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
]


ROOT_URLCONF = 'notion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.blog.context_processor.generic',
            ],
        },
    },
]

WSGI_APPLICATION = 'notion.wsgi.application'

DATABASES = {
    'default': env.db(),
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles')
]

LANGUAGES = (
    ('ru', _('Russian')),
    ('en', _('English')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

MAX_LOG_FILE_SIZE = 1024 * 1024 * 50  # 50 megabytes

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s]: %(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'formatter': 'verbose',
            'class': 'logging.StreamHandler'
        },
        'file_handler': {
            'filename': os.path.join(BASE_DIR, 'logs', 'notion.log'),
            'class': 'logging.handlers.RotatingFileHandler',
            'encoding': 'utf-8',
            'formatter': 'verbose',
            'maxBytes': MAX_LOG_FILE_SIZE,
            'backupCount': 20,
        },
        'null': {
            'class': 'logging.NullHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file_handler'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '..', 'uploads')

REDACTOR_UPLOAD = 'redactor/'
REDACTOR_OPTIONS = {'lang': 'ru'}

MEDIA_URL = '/uploads/'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        },
        'KEY_PREFIX': 'notion'
    }
}

