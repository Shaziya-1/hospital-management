"""
Django settings for hospitalmanagement project.
Optimized for Azure App Service deployment and local development.
"""

import os
from pathlib import Path

# ---------------------------------------------------------------------
# BASE DIRECTORIES
# ---------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / 'templates'
STATIC_DIR = BASE_DIR / 'static'
MEDIA_DIR = BASE_DIR / 'media'

# ---------------------------------------------------------------------
# SECURITY SETTINGS
# ---------------------------------------------------------------------
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-secure-secret-key')

# ✅ Debug mode — turn False in production (set in Azure Configuration)
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

ALLOWED_HOSTS = [
    'hospitalsystem-hzbfh9ddh2b9eecy.centralindia-01.azurewebsites.net',
    '.azurewebsites.net',
    'localhost',
    '127.0.0.1',
]

# ✅ CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    'https://hospitalsystem-hzbfh9ddh2b9eecy.centralindia-01.azurewebsites.net',
    'https://*.centralindia-01.azurewebsites.net',
]

# ✅ HTTPS / Security headers
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', 'False').lower() == 'true'
SESSION_COOKIE_SECURE = False  # Set True only in Azure
CSRF_COOKIE_SECURE = False     # Set True only in Azure

# ---------------------------------------------------------------------
# APPLICATION DEFINITION
# ---------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local app
    'hospital',

    # Third-party
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Efficient static file serving
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hospitalmanagement.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'hospitalmanagement.wsgi.application'

# ---------------------------------------------------------------------
# DATABASE CONFIGURATION (SQLite for local, PostgreSQL for Azure)
# ---------------------------------------------------------------------
if os.getenv('RUNNING_ON_AZURE', '').lower() == 'true':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', 'hospital_db'),
            'USER': os.environ.get('DB_USER', 'hospitaladmin@hospitalsystem-shaziya-db'),
            'PASSWORD': os.environ.get('DB_PASSWORD', 'Shaziy@1432'),
            'HOST': os.environ.get('DB_HOST', 'hospitalsystem-shaziya-db.postgres.database.azure.com'),
            'PORT': os.environ.get('DB_PORT', '5432'),
            'OPTIONS': {
                'sslmode': 'require',
            },
        }
    }
else:
    # Local SQLite database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ---------------------------------------------------------------------
# PASSWORD VALIDATION
# ---------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------------------------------------------------------------
# INTERNATIONALIZATION
# ---------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# ---------------------------------------------------------------------
# STATIC & MEDIA FILES
# ---------------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR

# ---------------------------------------------------------------------
# LOGIN & EMAIL
# ---------------------------------------------------------------------
LOGIN_REDIRECT_URL = '/afterlogin'
LOGOUT_REDIRECT_URL = '/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ---------------------------------------------------------------------
# DEFAULT AUTO FIELD
# ---------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
