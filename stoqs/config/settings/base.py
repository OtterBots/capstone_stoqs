"""
Base settings to build other settings files upon.
"""
from pathlib import Path

import environ
from email.utils import getaddresses

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

# stoqs/
APPS_DIR = BASE_DIR / "stoqs"
env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(BASE_DIR / ".env"))


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# Need to set environment variable DATABASE_URL containing DB login/password
# e.g.: export DATABASE_URL="postgis://stoqsadm:CHANGEME@127.0.0.1:5432/stoqs"
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': env.db("DATABASE_URL")
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

DEFAULT_AUTO_FIELD='django.db.models.AutoField'

# Functional tests require a separate MAPSERVER_DATABASE_URL setting
MAPSERVER_DATABASE_URL = env('MAPSERVER_DATABASE_URL', default=env('DATABASE_URL'))
if MAPSERVER_DATABASE_URL == env('DATABASE_URL'):
    MAPSERVER_DATABASES = DATABASES.copy()
else:
    MAPSERVER_DATABASES = {
        'default': env.db("MAPSERVER_DATABASE_URL")
    }
    MAPSERVER_DATABASES['default']['ATOMIC_REQUESTS'] = True
    
# For running additional databases append entries from STOQS_CAMPAIGNS environment
# Example: export STOQS_CAMPAIGNS='stoqs_beds_canyon_events_t,stoqs_os2015_t'
for campaign in env.list('STOQS_CAMPAIGNS', default=[]):
    DATABASES[campaign] = DATABASES.get('default').copy()
    DATABASES[campaign]['NAME'] = campaign
    MAPSERVER_DATABASES[campaign] = MAPSERVER_DATABASES.get('default').copy()
    MAPSERVER_DATABASES[campaign]['NAME'] = campaign
    
# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
# STOQS assumes all times are GMT, which is the timezone of the database
# It's OK to use naiive datetimes with this policy
USE_TZ = False

# See: https://docs.djangoproject.com/en/3.0/ref/contrib/gis/install/geolibs/#geos-library-path
#      https://docs.djangoproject.com/en/3.0/ref/contrib/gis/install/geolibs/#gdal-library-path
# Default paths set to 'built from source' locations
GEOS_LIBRARY_PATH = env('GEOS_LIBRARY_PATH', default='/usr/local/lib/libgeos_c.so')
GDAL_LIBRARY_PATH = env('GDAL_LIBRARY_PATH', default='/usr/local/lib/libgdal.so')


# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
# DEBUG = env.bool("DJANGO_DEBUG", False)
# # Local time zone. Choices are
# # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# # though not all of them may be available with every OS.
# # In Windows, this must be set to your system time zone.
# TIME_ZONE = "UTC"
# # https://docs.djangoproject.com/en/dev/ref/settings/#language-code
# LANGUAGE_CODE = "en-us"
# # https://docs.djangoproject.com/en/dev/ref/settings/#languages
# # from django.utils.translation import gettext_lazy as _
# # LANGUAGES = [
# #     ('en', _('English')),
# #     ('pt-br', _('Português')),
# # ]
# # https://docs.djangoproject.com/en/dev/ref/settings/#site-id
# SITE_ID = 1
# # https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
# USE_I18N = True
# # https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
# USE_TZ = True
# # https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
# LOCALE_PATHS = [str(BASE_DIR / "locale")]

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
# DATABASES = {"default": env.db("DATABASE_URL")}
# DATABASES["default"]["ATOMIC_REQUESTS"] = True
# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize", # Handy template tags
    "django.contrib.admin",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "drf_spectacular",
]

LOCAL_APPS = [
    "stoqs.users",
    # Your stuff: custom apps go here
    "stoqs.stoqs",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {"sites": "stoqs.contrib.sites.migrations"}

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "users:redirect"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "account_login"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'stoqs.db_router.RouterMiddleware',
]

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", default=True)

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(BASE_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(APPS_DIR / "static")]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
# https://django-compressor.readthedocs.io/en/latest/quickstart/#installation
INSTALLED_APPS += ["compressor"]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR / "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"



# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#dirs
        "DIRS": [str(APPS_DIR / "templates/stoqs")],
        # https://docs.djangoproject.com/en/dev/ref/settings/#app-dirs
        "APP_DIRS": True,
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "stoqs.users.context_processors.allauth_settings",
            ],
        },
    }
]

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
EMAIL_USE_TLS = env('EMAIL_USE_TLS', default=True)
EMAIL_HOST = env('EMAIL_HOST', default='mbarimail.mbari.org')
EMAIL_PORT = env('EMAIL_PORT', default=587)
EMAIL_HOST_USER = env('EMAIL_HOST_USE', default='stoqsadm')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
# In the format 'Full Name <email@example.com>, Full Name <anotheremail@example.com>'
# e.g. DJANGO_ADMINS=Full Name <email-with-name@example.com>,anotheremailwithoutname@example.com
ADMINS = getaddresses([env('DJANGO_ADMINS', default='Super User <root@localhost>')])

# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'


# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console_debug_false': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console_debug_false'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# For a development system (Vagrant) we use insecure apache which is http and the default
# Docker uses a proxy through nginx which provides https (set in docker-compose.yml)
MAPSERVER_SCHEME = env('MAPSERVER_SCHEME', default='http')

# Must be externally accessible if your STOQS server is to be externally accessible
# The default of 'localhost:8080' is for a Vagrant install, set MAPSERVER_HOST for
# other cases, e.g. export MAPSERVER_HOST='172.16.130.204:80'
MAPSERVER_HOST = env('MAPSERVER_HOST', default='localhost:8080')

# For template generated .map files, the URL_ version is for Docker shared volume setup
MAPFILE_DIR = env('MAPFILE_DIR', default='/dev/shm')
URL_MAPFILE_DIR = env('URL_MAPFILE_DIR', default='/dev/shm')

# To allow running Jupyter notebooks in Vagrant's or Docker's host browser
# See: https://fsdev.io/how-to-install-jupyter-notebook-in-a-dockerized-django-project/
NOTEBOOK_ARGUMENTS = [
    '--ip', '0.0.0.0',
    '--port', '8888',
    '--allow-root',
    '--no-browser',
]

# STOQS specific logging
LOGGING['formatters'] = {
    'veryverbose': {
        'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(filename)s %(funcName)s():%(lineno)d %(message)s'
    },
    'verbose': {
        'format': '%(levelname)s %(asctime)s %(filename)s %(funcName)s():%(lineno)d %(message)s'
    },
    'simple': {
        'format': '%(levelname)s %(message)s'
    },
}
LOGGING['handlers']['console'] = {
                            'level':'DEBUG',
                            'class':'logging.StreamHandler',
                            'formatter': 'verbose'
}
LOGGING['loggers']['stoqs'] = {
                            'handlers':['console'],
                            'level':'INFO',
                            'formatter': 'verbose'
}
LOGGING['loggers']['stoqs.db_router'] = {
                            'handlers':['console'],
                            'propagate': True,
                            'level':'INFO',
                            'formatter': 'verbose'
}
LOGGING['loggers']['loaders'] = {
                            'handlers':['console'],
                            'propagate': True,
                            'level':'INFO',
                            'formatter': 'verbose'
}
LOGGING['loggers']['utils'] = {
                            'handlers':['console'],
                            'propagate': True,
                            'level':'INFO',
                            'formatter': 'verbose'
}
LOGGING['loggers']['stoqs.views'] = {
                            'handlers':['console'],
                            'level':'INFO',
                            'formatter': 'verbose'
}
LOGGING['loggers']['stoqs.tests'] = {
                            'handlers':['console'],
                            'level':'INFO',
                            'formatter': 'verbose'
}
LOGGING['loggers']['__main__'] = {
                            'handlers':['console'],
                            'level':'INFO',
                            'formatter': 'verbose'
}
LOGGING['loggers']['stoqs']['level'] = 'INFO'

# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = "username"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ADAPTER = "stoqs.users.adapters.AccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/forms.html
ACCOUNT_FORMS = {"signup": "stoqs.users.forms.UserSignupForm"}
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_ADAPTER = "stoqs.users.adapters.SocialAccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/forms.html
SOCIALACCOUNT_FORMS = {"signup": "stoqs.users.forms.UserSocialSignupForm"}

# django-rest-framework
# -------------------------------------------------------------------------------
# django-rest-framework - https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup
CORS_URLS_REGEX = r"^/api/.*$"

# By Default swagger ui is available only to admin user(s). You can change permission classes to change that
# See more configuration options at https://drf-spectacular.readthedocs.io/en/latest/settings.html#settings
SPECTACULAR_SETTINGS = {
    "TITLE": "stoqs API",
    "DESCRIPTION": "Documentation of API endpoints of stoqs",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
}
# Your stuff...
# ------------------------------------------------------------------------------
