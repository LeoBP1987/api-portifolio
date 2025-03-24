from pathlib import Path, os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portifolio',
    'rest_framework',
    'storages',
]

# Atualizando base de usuarios customizados
AUTH_USER_MODEL = 'portifolio.UsuariosCustomizados'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'setup.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'setup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('URLPOSTGRES'),
        conn_max_age=600,
        ssl_require=True
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Configurança arquivos estáticos e media

STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "access_key": str(os.getenv("R2_ACCESS_KEY_ID")),
                "secret_key": str(os.getenv("R2_SECRET_ACCESS_KEY")),
                "bucket_name": str(os.getenv("R2_STORAGE_BUCKET_NAME")),
                "endpoint_url": "https://626ebd951efc663e718a48a8fcc0dce5.r2.cloudflarestorage.com/",
                "custom_domain": str(os.getenv("R2_CUSTOM_DOMAIN")),
                "location": "static",  
            },
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "access_key": str(os.getenv("R2_ACCESS_KEY_ID")),
                "secret_key": str(os.getenv("R2_SECRET_ACCESS_KEY")),
                "bucket_name": str(os.getenv("R2_STORAGE_BUCKET_NAME")),
                "endpoint_url": str(os.getenv("R2_ENDPOINT")),
                "custom_domain": str(os.getenv("R2_ENDPOINT_PUBLIC")),
                "location": "static", 
            },
        },
    }


AWS_DEFAULT_ACL = 'public-read'

AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

AWS_LOCATION = 'static'

AWS_QUERYSTRING_AUTH = False

AWS_HEADER = {
        'Access-Control-Allow-Origin': '*',
    }

STATIC_URL = f'https://{os.getenv("R2_ENDPOINT_PUBLIC")}/static/'

MEDIA_URL = f'https://{os.getenv("R2_ENDPOINT_PUBLIC")}/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
