
import os

#DEBUG = True

STATIC_URL = 'http://cdn.bergqvi.st/pipiki/static/'

MEDIA_URL = 'http://cdn.bergqvi.st/pipiki/static/'

SITE_ID = 1


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTUSER'),
        'HOST': os.getenv('POSTHOST'),
        'USER': os.getenv('POSTUSER'),
        #    'PORT': 33060,
        'PASSWORD': os.getenv('POSTPASSWORD'),
        }
}