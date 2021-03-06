import os
from urlparse import urlparse

DEBUG = True
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'Europe/Stockholm'

LANGUAGE_CODE = 'sv-SE'

SITE_ID = 1

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

try:
    MEDIA_ROOT = os.path.join(os.environ["GONDOR_DATA_DIR"], "site_media", "media")
except :
    pass

try:
    STATIC_ROOT = os.path.join(os.environ["GONDOR_DATA_DIR"], "site_media", "static")
except :
    pass

STATIC_URL = 'http://cdn.bergqvi.st/pipiki/static/'
#STATIC_URL = 'http://pipiki.s3-website-eu-west-1.amazonaws.com/'

MEDIA_URL = '/media/'

# Additional locations of static files
STATICFILES_DIRS = (
#    os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static'),
    os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pipiki'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_URL = 'http://cdn.bergqvi.st/pipiki/static/'
#COMPRESS_URL = 'http://pipiki.s3-website-eu-west-1.amazonaws.com/'
#STATIC_URL = COMPRESS_URL
#COMPRESS_URL = '/static/'
#COMPRESS_OFFLINE_CONTEXT = {
#    'STATIC_URL': STATIC_URL,
#    'MEDIA_URL': MEDIA_URL,
#}

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pipiki/static')
#COMPRESS_OUTPUT_DIR = '/media/cache'
#COMPRESS_STORAGE = 'pipiki.storage.CachedSFTPStorage'
STATICFILES_STORAGE = 'storages.backends.sftpstorage.SFTPStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.sftpstorage.SFTPStorage'

#STATICFILES_STORAGE = 'pipiki.storage.CachedSFTPStorage'
#DEFAULT_FILE_STORAGE = 'pipiki.storage.CachedSFTPStorage'

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

if os.environ.has_key('AWS_ACCESS_KEY_ID'):
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')


# List of callables that know how to import templates from various sources.
#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.load_template_source',
#    'django.template.loaders.app_directories.load_template_source',
##     'django.template.loaders.eggs.load_template_source',
#)

TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader"
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'flatpages.middleware.FlatpageFallbackMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
#    'articles.middleware.dynamicsites.DynamicSiteIDMiddleware',
)

#For the dynamicsites middleware
CREATE_SITES_AUTOMATICALLY = False

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
#    'templates/',
#    'genericdropdown/templates',
#    'templates/flatpages/',
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
    os.path.join(os.path.dirname(__file__), 'genericdropdown/templates').replace('\\','/'),
)


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.syndication',
    'django.contrib.comments',
    'django.contrib.staticfiles',
#    'requests',
    'articles',
    'south',
    # 'sitetree',
    'mptt',
    'treenav',
    # 'genericadmin',
#    'compressor',
    'sorl.thumbnail',
#    'disqus',
    'flatpages',
    'django_wysiwyg',
    'debug_toolbar',
    'django_extensions',
    'storages',
    'compressor',
)

DJANGO_WYSIWYG_FLAVOR = "ckeditor"
ARTICLES_AUTO_TAG = False

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
)

SITES_DIR = os.path.join(os.path.dirname(__file__), 'sites')

if os.environ.has_key('FTPSTORAGE'):
    url = urlparse(os.getenv('FTPSTORAGE'))

    SFTP_STORAGE_HOST = url.hostname
    SFTP_STORAGE_ROOT = '/var/www/cdn/pipiki/'
    SFTP_STORAGE_PARAMS = {
        'username': url.username,
        'password': url.password
    }
    SFTP_KNOWN_HOST_FILE = os.path.join(MEDIA_ROOT, "ssh", "known_hosts")

    if not os.path.exists(os.path.join(MEDIA_ROOT, "ssh")):
        os.makedirs(os.path.join(MEDIA_ROOT, "ssh"))
        f = file(SFTP_KNOWN_HOST_FILE, "w")
        f.close()


if os.environ.has_key('EMAIL_HOST'):

    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = os.getenv('EMAIL_PORT')
    EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')

    ADMINS = (('Peppe', 'p@bergqvi.st'), )
    MANAGERS = ADMINS

try:
    from local_settings import *
except ImportError:
    pass
