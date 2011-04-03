import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'Europe/Stockholm'

LANGUAGE_CODE = 'sv-SE'

SITE_ID = 1

MEDIA_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'



# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
                 "templates/"
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
    
    'articles',
    # 'south',
    # 'sitetree',
    'mptt',
    'treenav',
    # 'genericadmin',

)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
)


#########################################################################
# Import settings from local_settings.py, if it exists.
#
# Put this at the end of settings.py

try:
    import local_settings
except ImportError:
    print """ 
        -------------------------------------------------------------------------
        You need to create a local_settings.py file which needs to contain at least
        database connection information.

        Copy local_settings_example.py to local_settings.py and edit it.
        -------------------------------------------------------------------------
        """
    import sys 
    sys.exit(1)
else:
    # Import any symbols that begin with A-Z. Append to lists any symbols that
    # begin with "EXTRA_".
    import re
    for attr in dir(local_settings):
        # print attr
        match = re.search('^EXTRA_(\w+)', attr)
        if match:
            # print "match"
            name = match.group(1)
            value = getattr(local_settings, attr)
            try:
                globals()[name] += value
            except KeyError:
                globals()[name] = value
        elif re.search('^[A-Z]', attr):
            globals()[attr] = getattr(local_settings, attr)  
