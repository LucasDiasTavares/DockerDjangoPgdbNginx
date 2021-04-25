mport os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['DomainNameHere', 'DomainIPHereIfWanna']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'colorfield',
    'customAPIHere',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = [
        'GET',
]

CORS_ALLOW_HEADERS = [
        'accept',
        'accept-encoding',
        'authorization',
        'Authorization',
        'content-type',
        'dnt',
	    'origin',
        'user-agent',
        'x-csrftoken',
        'x-requested-with',
]


ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
     	'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
	},
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('NAME'),
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
        'HOST': config('HOST'),
        'PORT': config('PORT'),
    }
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

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/static/'
STATIC_ROOT = '/vol/web/static/'

MEDIA_URL = '/static/media/'
MEDIA_ROOT = '/vol/web/media'
