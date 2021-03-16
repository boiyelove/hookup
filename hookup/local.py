import os

EMAIL_BACKEND = "mailer.backend.DbBackend"
MAILER_EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_MAIL = 'notifications@localhost'
ALLOWED_HOSTS = ['localhost:8001','127.0.0.1:8001','localhost']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'pstatic'),]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = ''

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

USE_CDN = False

ALLOWED_HOSTS = ['*']