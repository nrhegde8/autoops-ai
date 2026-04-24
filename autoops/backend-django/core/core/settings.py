from pathlib import Path
import os
from dotenv import load_dotenv

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv()

# SECURITY
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-dev-key")
DEBUG = True
ALLOWED_HOSTS = []

# ================= APPS =================
INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'orders',
]

# ================= MIDDLEWARE =================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

# ================= TEMPLATES =================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'

# ================= DATABASE =================
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

if not DB_NAME or not DB_USER:
    raise ValueError("Database environment variables not set properly")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# ================= PASSWORD VALIDATION =================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ================= INTERNATIONAL =================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ================= STATIC =================
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ================= CORS =================
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = ["*"]
CORS_ALLOW_METHODS = ["*"]

# ================= 🔥 CRITICAL FIX =================
# 🚀 THIS LINE REMOVES AUTH COMPLETELY

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
}