from pathlib import Path
from dotenv import load_dotenv
from corsheaders.defaults import default_headers
import dj_database_url
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['api-portifolio-f4f0784e5e08.herokuapp.com', 'localhost', '127.0.0.1']


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
    'django_filters',
    'oauth2_provider',
    'corsheaders',
]

# Atualizando base de usuarios customizados
AUTH_USER_MODEL = 'portifolio.UsuariosCustomizados'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
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
                "endpoint_url": str(os.getenv("R2_ENDPOINT")),
                "custom_domain": str(os.getenv("R2_ENDPOINT_PUBLIC")),
                "location": "media",  
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

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuração de Permissões e Autenticações
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ]
}

AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://portifolio-7yj0wb5z0-leonardos-projects-c279e19b.vercel.app/",
    "https://portifolio-git-main-leonardos-projects-c279e19b.vercel.app/",
    "https://portifolio-leonardo-pereira.vercel.app/"
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'Content-Type',
    'Authorization',
]

# Configuração de envio de EMAIL
EMAIL_BACKEND = str(os.getenv('EMAIL_BACKEND'))
EMAIL_HOST = str(os.getenv('EMAIL_HOST'))
EMAIL_PORT = str(os.getenv('EMAIL_PORT'))
EMAIL_USE_TLS = str(os.getenv('EMAIL_USE_TLS'))
EMAIL_HOST_USER = str(os.getenv('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD = str(os.getenv('EMAIL_HOST_PASSWORD'))
DEFAULT_FROM_EMAIL = str(os.getenv('DEFAULT_FROM_EMAIL'))