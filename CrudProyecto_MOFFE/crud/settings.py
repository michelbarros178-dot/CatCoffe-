"""
Django settings for crud project.
"""

from pathlib import Path
import os
import pymysql

# Configuración del conector para XAMPP (solo se usa si no hay DATABASE_URL)
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-ce=(80ay2tk!f913xkdv&)7e2gbj1omls-8ojl##)g75&k8c(=')
# En producción, siempre usar variable de entorno SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
# Por defecto True en local (si no se define), pero en Vercel pondremos DEBUG=False

# Permitir hosts: localhost, 127.0.0.1, y dominios de Vercel
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.vercel.app', 'tu-dominio.com']  # ajusta tu dominio

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'productos',  # Tu aplicación de productos
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Añadido (debe ir después de Security)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Ruta para tus carpetas de HTML
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

WSGI_APPLICATION = 'crud.wsgi.application'

# Database - Configuración flexible: si existe DATABASE_URL, la usa; si no, usa XAMPP
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    # Producción (Vercel) - usando dj-database-url
    DATABASES = {
        'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600)
    }
else:
    # Desarrollo local con XAMPP (MySQL)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'db_moffee',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '3307',
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization - Configurado para Colombia
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"
# Configuración para WhiteNoise (compresión y caché)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (Imágenes de mascotas, etc.)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Redirecciones de autenticación
LOGIN_REDIRECT_URL = 'inicio'
LOGOUT_REDIRECT_URL = 'login'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Parche de compatibilidad definitiva para MariaDB 10.4 (solo si es necesario)
# Esto solo se aplica si estamos usando MySQL/MariaDB en local.
# Si usamos PostgreSQL en producción, no afecta.
if not DATABASE_URL:
    from django.db.backends.mysql.features import DatabaseFeatures
    DatabaseFeatures.can_return_columns_from_insert = property(lambda x: False)
    DatabaseFeatures.can_return_rows_from_bulk_insert = property(lambda x: False)
    import django.db.backends.mysql.base
    django.db.backends.mysql.base.DatabaseWrapper.check_database_version_supported = lambda x: None