"""
SmartBoard 360 – Django Settings
"""

import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

# ─────────────────────────────────────────────────────────────────────
# Base directory and environment variables
# ─────────────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env
load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'fallback-secret-key'
)

DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']


# ─────────────────────────────────────────────────────────────────────
# Installed Apps
# ─────────────────────────────────────────────────────────────────────

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'channels',

    # Local Apps
    'apps.accounts',
    'apps.notices',
    'apps.reminders',
    'apps.staff',
    'apps.timetable',
]


# ─────────────────────────────────────────────────────────────────────
# Middleware
# ─────────────────────────────────────────────────────────────────────

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ─────────────────────────────────────────────────────────────────────
# URLs
# ─────────────────────────────────────────────────────────────────────

ROOT_URLCONF = 'config.urls'


# ─────────────────────────────────────────────────────────────────────
# Templates
# ─────────────────────────────────────────────────────────────────────

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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


# ─────────────────────────────────────────────────────────────────────
# ASGI / WSGI
# ─────────────────────────────────────────────────────────────────────

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'


# ─────────────────────────────────────────────────────────────────────
# Database – AWS RDS MySQL
# ─────────────────────────────────────────────────────────────────────

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',

        # RDS database name
        'NAME': os.getenv('DB_NAME', 'dnbdb'),

        # RDS database username
        'USER': os.getenv('DB_USER', 'dnbadmin'),

        # RDS database password
        'PASSWORD': os.getenv('DB_PASSWORD', ''),

        # RDS endpoint
        'HOST': os.getenv('DB_HOST', ''),

        # MySQL port
        'PORT': os.getenv('DB_PORT', '3306'),

        # Keep database connection alive
        'CONN_MAX_AGE': 60,

        'OPTIONS': {
            'connect_timeout': 10,
        },
    }
}


# ─────────────────────────────────────────────────────────────────────
# Cache
# ─────────────────────────────────────────────────────────────────────

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'smartboard360-cache',
        'TIMEOUT': 30,
        'OPTIONS': {
            'MAX_ENTRIES': 1000,
        },
    }
}


# ─────────────────────────────────────────────────────────────────────
# Password Validation
# ─────────────────────────────────────────────────────────────────────

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator'
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator'
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator'
    },
]


# ─────────────────────────────────────────────────────────────────────
# Internationalization
# ─────────────────────────────────────────────────────────────────────

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# ─────────────────────────────────────────────────────────────────────
# Static / Media
# ─────────────────────────────────────────────────────────────────────

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ─────────────────────────────────────────────────────────────────────
# Custom User Model
# ─────────────────────────────────────────────────────────────────────

AUTH_USER_MODEL = 'accounts.User'


# ─────────────────────────────────────────────────────────────────────
# Django REST Framework
# ─────────────────────────────────────────────────────────────────────

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}


# ─────────────────────────────────────────────────────────────────────
# JWT
# ─────────────────────────────────────────────────────────────────────

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),

    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),

    'ROTATE_REFRESH_TOKENS': True,

    'AUTH_HEADER_TYPES': ('Bearer',),
}


# ─────────────────────────────────────────────────────────────────────
# CORS
# ─────────────────────────────────────────────────────────────────────

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

CORS_ALLOW_CREDENTIALS = True

# Temporary setting for deployment/testing
CORS_ALLOW_ALL_ORIGINS = True

# Apply CORS headers to media files
CORS_URLS_REGEX = r'^.*$'


# ─────────────────────────────────────────────────────────────────────
# Django Channels
# ─────────────────────────────────────────────────────────────────────

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}


# ─────────────────────────────────────────────────────────────────────
# Email – Gmail SMTP
# ─────────────────────────────────────────────────────────────────────

EMAIL_BACKEND = (
    'django.core.mail.backends.smtp.EmailBackend'
)

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.getenv(
    'EMAIL_HOST_USER',
    ''
).strip()

EMAIL_HOST_PASSWORD = os.getenv(
    'EMAIL_HOST_PASSWORD',
    ''
).strip()

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# ─────────────────────────────────────────────────────────────────────
# Frontend URL
# ─────────────────────────────────────────────────────────────────────

FRONTEND_URL = os.getenv(
    'FRONTEND_URL',
    'http://localhost:3000'
)
