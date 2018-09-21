import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


    
ALLOWED_HOSTS = ['hookup.boiyelove.com']
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_FROM_EMAIL = 'notifications@boiyelove.com'
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_PASSWORD = '0k@yITHANK,w1ll;'
EMAIL_HOST_USER = 'boiyeclient'
EMAIL_PORT = '25'
SERVER_EMAIL = 'notifications@boiyelove.com'


PROD = True

STATIC_URL = '/static/hookup/'
MEDIA_URL = '/media/hookup/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates/pstatic'),]
STATIC_ROOT = '/home/boiyelove/webapps/staticfiles/hookup/'
MEDIA_ROOT = '/home/boiyelove/webapps/mediafiles/hookup/'
EXPORT_ROOT = MEDIA_ROOT + 'exports/'


WEBSITE_ADDR = 'http://hookup.boiyelove.com'

#Read secret key from a file
with open(os.path.join(BASE_DIR,'hookup/secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

USE_CDN = True