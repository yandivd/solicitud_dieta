# -*- coding: utf-8 -*-
"""
Django settings for control_tfa_apa project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import pymysql
pymysql.install_as_MySQLdb()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#import ldap
# from django_auth_ldap.config import LDAPSearch

# AUTH_LDAP_SERVER_URI = 'ldap://192.168.91.114:389'
# AUTH_LDAP_BIND_DN = "uid=solicitudpago.dtar,ou=etecsa.cu,ou=People,dc=etecsa,dc=cu"
# AUTH_LDAP_BIND_PASSWORD = "TIapp*2022"
# AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=etecsa.cu,ou=People,dc=etecsa,dc=cu"
# AUTH_LDAP_USER_ATTR_MAP = {
#                 "first_name": "givenName",
#                 "last_name": "sn",
#                 "email": "mail",
# }
# AUTHENTICATION_BACKENDS = [
#             'django.contrib.auth.backends.ModelBackend',
#             'django_auth_ldap.backend.LDAPBackend',          
# ]
# os.environ['PYTHON_EGG_CACHE'] = '/var/www/html/'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y%2+cy4at3#zy%%5nxl#-5sr-gq&2r2x8@(hrxd#tgn)28g&h3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'smart_selects',
    # 'django_crontab',
    # 'django_cleanup.apps.CleanupConfig',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'solicitud_dietas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'solicitud_dietas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': 'db_dieta',
#         'USER': 'root',
#         'PASSWORD': 'Seguimos/25',
#         'HOST': 'localhost',
#         'PORT': '80',
#     }
# }


# DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': 'db_dietas',
#             'USER': 'root',
#             'PASSWORD': 'L3n0v0*23',
#             'HOST': 'localhost',
#             'PORT': '3306',
#         }
# }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N =False

USE_TZ = False

#DATETIME_FORMAT='%Y-%m-%d %H:%M:%S'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.etecsa.cu'
EMAIL_HOST_USER = 'solicitudpago.dtar@etecsa.cu'
EMAIL_HOST_PASSWORD ='TIapp*2022'
EMAIL_PORT = 587

SESSION_COOKIE_NAME = 'session_solicitud_dieta'
CSRF_COOKIE_NAME  ='csrf_solicitud_dieta'
USE_THOUSAND_SEPARATOR = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/estaticos_solicitud_dieta/'
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media_solicitud_dieta/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


USE_DJANGO_JQUERY = True
JAZZMIN_SETTINGS = {
    # title of the window
    "site_title": "Solicitud de Dieta",

    # Title on the brand, and the login screen (19 chars max)
    "site_header": "Solicitud de Dieta",

    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    #"site_logo": "books/img/logo.png",

    # Welcome text on the login screen
    "welcome_sign": "Bienvenido al sitio de administración",

    # Copyright on the footer
    #"copyright": "TI-DTAR",

    # The model admin to search from the search bar, search bar omitted if excluded
    #"search_model": "auth.User",

    # Field name on user model that contains avatar image
    "user_avatar": None,

    ############
    # Top Menu #
    ############
    
    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Solicitudes de Dieta",  "url": "/"},

        # external url that opens in a new window (Permissions can be added)
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "app"},
    ],
    
    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": False,

    # Whether to aut expand the menu
    "navigation_expanded": False,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth"],

    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "books": [{
            "name": "Make Messages", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free
    # for a list of icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    #"custom_css": None,
    "custom_js": '/scripts.js',
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "vertical_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "horizontal_tabs", "auth.group": "vertical_tabs","app.tcp": "horizontal_tabs"},
    # Add a language dropdown into the admin
    #"language_chooser": True,
}
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    }
}
