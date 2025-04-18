from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#cs1=7)8%cw64qmrf+p0_3k1-2$g^l-86t$*dzf7zo4zppyyi$"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wagtaildb',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db', # Matches the service name in docker-compose.yml
        'PORT': '5432',
    }
}



EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
