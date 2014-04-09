# -*- coding: utf-8 -*-
# Django settings for profsoux project.
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Mikhail Baranov', 'dev@brnv.ru'),
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',     # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_ROOT, 'data.db'),                          # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

USE_THOUSAND_SEPARATOR = True

NUMBER_GROUPING = 3

THOUSAND_SEPARATOR = " "

LANGUAGE_CODE = 'ru-RU'

FIRST_DAY_OF_WEEK = 1

DATE_FORMAT = 'd E Y'

DATE_INPUT_FORMATS = ('%d.%m.%Y', '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y',
                      '%b %d %Y', '%b %d, %Y', '%d %b %Y', '%d %b, %Y',
                      '%B %d %Y', '%B %d, %Y', '%d %B %Y', '%d %B, %Y')

DATETIME_FORMAT = 'd E Y H:i'

DATETIME_INPUT_FORMATS = ('%d.%m.%Y %H:%M', '%d.%m.%Y %H:%M:%S',
                          '%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d',
                          '%m/%d/%Y %H:%M:%S', '%m/%d/%Y %H:%M', '%m/%d/%Y',
                          '%m/%d/%y %H:%M:%S', '%m/%d/%y %H:%M', '%m/%d/%y')

TIME_FORMAT = 'H:i'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'uploads')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/uploads/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'
#STATIC_URL = 'http://static.profsoux.ru/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

# Additional locations of static files
STATICFILES_DIRS = (
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0rda)md)mwiny^z!-v2b)t2m-6*j$=m=f)ql4_+s6!&e+#l-zo'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'conference.middleware.EventMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",

    "django.core.context_processors.media",
    "django.core.context_processors.static",

    'django.core.context_processors.request',

    'utils.context_processors.site_globals',
)

ROOT_URLCONF = 'profsoux.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'filebrowser',
    'grappelli',

    'django.contrib.admin',
    'django.contrib.flatpages',
    'south',

    'flatblocks',
    'conference',
    'registration',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
}

# TinyMCE Settings
TINYMCE_JS_URL = STATIC_URL + 'js/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = STATIC_URL + 'js/tiny_mce'

#TINYMCE_FILEBROWSER = False
TINYMCE_DEFAULT_CONFIG = {
    #'mode' : "textareas",
    #'theme': "advanced",
    #'theme_advanced_toolbar_location' : "top",
    #'theme_advanced_resizing' : True,
    'extended_valid_elements': "article[name|href|target|title|onclick],section",
    }


# Filebrowser Settings
FILEBROWSER_DIRECTORY = MEDIA_ROOT

EMAIL_SUBJECT_PREFIX = "[Profsoux.ru] "

SEND_BROKEN_LINK_EMAILS = True

SERVER_EMAIL = 'server@profsoux.ru'

AKISMET_KEY = '062e97a17ef0'
