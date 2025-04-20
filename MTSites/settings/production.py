from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
    }
}

ALLOWED_HOSTS = [
    '*',
]
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', default='django-insecure-!@#qwe1234')
# CRSF_TRUSTED_ORIGINS 
CRSF_TRUSTED_ORIGINS = [
    'localhost',
]    

# Add whitenoise to INSTALLED_APPS
INSTALLED_APPS = ['whitenoise.runserver_nostatic'] + INSTALLED_APPS

# Add whitenoise middleware
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Static files configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Ensure collectstatic works properly
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

# Media files configuration
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Whitenoise settings
WHITENOISE_MAX_AGE = 31536000  # 1 year in seconds

try:
    from .local import *
except ImportError:
    pass
