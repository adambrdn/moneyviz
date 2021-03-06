"""
Django settings for moneyviz project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rsy0*v!+d54v6vmde7ht*5h=jd%3+%blrw7sw#)71di#wub*aj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django_pdb',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'main',
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
)

ROOT_URLCONF = 'moneyviz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'moneyviz.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTHENTICATION_BACKENDS = (
   'social.backends.google.GoogleOAuth2',
   'django.contrib.auth.backends.ModelBackend'
)

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_PIPELINE = (
         'social.pipeline.social_auth.social_details',
         'social.pipeline.social_auth.social_uid',
         'social.pipeline.social_auth.auth_allowed',
         'social.pipeline.social_auth.social_user',
         'social.pipeline.user.get_username',
         'social.pipeline.user.create_user',
         'social.pipeline.social_auth.associate_user',
         'social.pipeline.social_auth.load_extra_data',
         'social.pipeline.user.user_details',
         'main.pipeline.save_avatar_url',
)

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
   os.path.join(BASE_DIR, "static"),
)

LOGDIR = os.path.join(BASE_DIR, 'logs')
LOGFILE = os.path.join(LOGDIR, 'site.log')
if not os.path.exists(LOGDIR):
   os.makedirs(LOGDIR)

if not os.path.isfile(LOGFILE):
   open(LOGFILE, 'w').close()

LOGGING = {
   'version' : 1,
   'disable_existing_loggers' : False,
   'formatters' : {
      'simple' : {
         'format' : '%(levelname)s %(message)s',
      },
   },
   'handlers' : {
      'file' : {
         'level' : 'DEBUG',
         'class' : 'logging.FileHandler',
         'filename' : LOGFILE,
         'formatter' : 'simple',
      }
   },
   'loggers' : {
      'main' : {
         'handlers' : ['file'],
         'level' : 'DEBUG',
         'propogate' : True,
      }
   }
}

SESSION_COOKIE_AGE = 7200

LOGIN_URL='/loginpage'
