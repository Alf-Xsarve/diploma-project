"""
Django settings for backende project.
"""

from pathlib import Path
import os
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-)imu2&r@(rd)ym@*ki#43x)7c7ztwi5h0)v5r#gueplm_&m-(^'
DEBUG = False
ALLOWED_HOSTS = ['*']

# -------------------------------
# MEDIA
# -------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# -------------------------------
# STATIC (🔥 ВАЖНО ДЛЯ REACT)
# -------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 👉 путь к React build (Vite)
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR.parent, 'frontend/dist'),
# ]

# -------------------------------
# TEMPLATES (🔥 для index.html)
# -------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 👈 добавили
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# -------------------------------
# APPS
# -------------------------------
INSTALLED_APPS = [
    'apps.persons',

    'rest_framework',
    'drf_yasg',

    'jazzmin',
    "corsheaders",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# -------------------------------
# MIDDLEWARE
# -------------------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",

    # 🔥 WhiteNoise
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.middleware.common.CommonMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

JAZZMIN_SETTINGS = {
    # 🔝 Заголовки
    "site_title": "История Кыргызстана",
    "site_header": "История Кыргызстана",
    "site_brand": "KG History",

    # 👋 Приветствие
    "welcome_sign": "Добро пожаловать в систему управления",
    "copyright": "© 2026 Дипломный проект",

    # 🔍 Поиск
    "search_model": ["persons.HistoricalPerson", "auth.User"],

    # 👤 аватар (можно потом добавить)
    "user_avatar": None,

    ################
    # TOP MENU ❌
    ################
    # УБИРАЕМ верхнее меню
    "topmenu_links": [],

    ################
    # USER MENU
    ################
    "usermenu_links": [
        {"name": "Профиль", "model": "auth.user"},
    ],

    ################
    # SIDEBAR ✅
    ################
    "show_sidebar": False,
    "navigation_expanded": True,  # компактный стиль

    # порядок
    "order_with_respect_to": [
        "persons",
        "persons.historicalperson",
        "persons.favorite",
        "auth",
    ],

    # кастомные ссылки
    "custom_links": {
        "persons": [
            {
                "name": "Все личности",
                "url": "/admin/persons/historicalperson/",
                "icon": "fas fa-users",
            },
        ]
    },

    ################
    # ICONS 🎨
    ################
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.group": "fas fa-users",

        "persons": "fas fa-landmark",
        "persons.historicalperson": "fas fa-monument",
        "persons.favorite": "fas fa-heart",
    },

    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    ################
    # MODAL
    ################
    "related_modal_active": True,

    ################
    # UI
    ################
    "theme": "cosmo",  # 🔥 лучший визуал
    "show_ui_builder": False,
    "use_google_fonts_cdn": True,

    ################
    # FORM VIEW
    ################
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "collapsible",
    }
}

ROOT_URLCONF = 'backende.urls'
WSGI_APPLICATION = 'backende.wsgi.application'

# -------------------------------
# DRF + JWT
# -------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# -------------------------------
# DATABASE
# -------------------------------
DATABASES = {
    'default': {

        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'db',
        'PORT': '5432',

        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------------
# SWAGGER
# -------------------------------
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

# -------------------------------
# PASSWORD VALIDATION
# -------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------------
# LOCALIZATION
# -------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------------
# CORS
# -------------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# -------------------------------
# WHITENOISE (🔥 ускорение)
# -------------------------------
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"