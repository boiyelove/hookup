import os

EMAIL_BACKEND = "mailer.backend.DbBackend"
MAILER_EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_MAIL = 'notifications@localhost'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates/pstatic'),]

MEDIA_ROOT = os.path.join('BASE_DIR', 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'pstatic')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

