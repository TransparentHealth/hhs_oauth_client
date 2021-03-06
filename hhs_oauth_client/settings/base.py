"""
Django settings for hhs_oauth_client project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.contrib.messages import constants as messages
from django.conf import global_settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join( BASE_DIR, '..')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'piehme*+^#hylq8uz2eszps%o!5!+*#1@+*83gmp$o(u3%!ldp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrapform',
    'apps.accounts',
    'apps.home',
    'apps.remotecalls',
    'apps.patient',
    'apps.provider',
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
     'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
)
ROOT_URLCONF = 'hhs_oauth_client.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                 os.path.join(BASE_DIR, 'templates'),
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect'


            ],
        },
    },
]

WSGI_APPLICATION = 'hhs_oauth_client.wsgi.application'


MESSAGE_TAGS ={ messages.DEBUG:   'debug',
                messages.INFO:    'info',
                messages.SUCCESS: 'success',
                messages.WARNING: 'warning',
                messages.ERROR:   'danger'
                }




# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'sitestatic'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MIN_PASSWORD_LEN = 8
AUTH_PROFILE_MODULE = 'accounts.UserProfile'
AUTHENTICATION_BACKENDS = (
            'django.contrib.auth.backends.ModelBackend',
            'apps.accounts.oauth_backends.myoauth.MyOAuthOAuth2'
            )



# python-social-auth settings
SOCIAL_AUTH_URL_NAMESPACE = 'social'

# instagram oauth
SOCIAL_AUTH_INSTAGRAM_KEY='38b495f6fa264851bd541ce183a58931'
SOCIAL_AUTH_INSTAGRAM_SECRET='2eeed20dab5e4241901e8afb518c4444'
SOCIAL_AUTH_INSTAGRAM_EXTRA_ARGUMENTS = {'scope': 'likes comments relationships'}


# myoauth oauth2
SOCIAL_AUTH_MYOAUTH_KEY = 'NNB95dtMtiIhwxf8amhXaJfHG8SFMC7bWxUFWqNa'
SOCIAL_AUTH_MYOAUTH_SECRET = 'wTupiam0f9IDXxHxOftLM18WLPSODdo0GL9OthcXwiS3zW8fl1VWr13lzFrW8jl7HQzxJnlu4WJfuLs9nnQiGyg0aYkASZun9M9PktYryN1lJm7zNemqeeZOiPLMDZdx'
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'
PROPRIETARY_BACKEND_NAME = 'myoauth'
# the trailing slash is necessary, because python-social-auth does not follow
# redirects by default.
HHS_OAUTH_URL = 'http://oauth:8000/'
MY_AUTHORIZATION_URL = 'http://oauth:8000/o/authorize/'
MY_ACCESS_TOKEN_URL =  'http://oauth:8000/o/token/'
MY_USER_PROFILE_URL =  'http://oauth:8000/profile/me'
LOGIN_URL          = '/accounts/login'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/accounts/login-error'


SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.debug.debug',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'social.pipeline.debug.debug'
)

try:
    from local import *
except:
    pass