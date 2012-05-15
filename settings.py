import os
import django

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

# Django settings for project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
#ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+t(q+ljogaj(+7m@kueu-g881gb8xp_oaz)$iabxjp8a1@2#u!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'finder.views.settings_processor',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'compressor',
    'tastypie',
    'boundaryservice',
    'finder',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

COMPRESS_ENABLED = False 

COMPRESS_ROOT = STATIC_ROOT

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Demo and site text values
EXAMPLE_SCOPE = 'Minnesota'

# Example boundary set values.
EXAMPLE_BOUNDARY_SET = 'Minnesota State House district'
EXAMPLE_BOUNDARY_SETS = 'Minnesota State House districts' # plural
EXAMPLE_BOUNDARY_SET_CODE = 'minnesota-state-house-districts'
EXAMPLE_BOUNDARY_SET_CODE_BIS = 'minnesota-state-house-districts-2002' # "bis" is latin for "again"
EXAMPLE_BOUNDARY_SET_RESPONSE = '''
{
  authority: "Minnesota GIS",
  boundaries: [ .. ],
  count: 134,
  domain: "Minnesota",
  href: "http://www.gis.leg.mn/redist2010/plans.html",
  last_updated: "2012-05-03",
  metadata_fields: [ .. ],
  name: "Minnesota State House districts",
  notes: "These districts were defined in 2012.",
  resource_uri: "/1.0/boundary-set/minnesota-state-house-districts/",
  slug: "minnesota-state-house-districts"
}
''' # an example JSON response

# Example boundary (within a boundary set)
EXAMPLE_BOUNDARY = 'Congressional district 4'
EXAMPLE_BOUNDARY_CODE = '4-congressional-district'
EXAMPLE_BOUNDARY_RESPONSE = '''
{
  centroid: {
    coordinates: [
      -92.9809341315504,
      45.00196132245185
    ],
    type: "Point"
  },
  external_id: "180077",
  kind: "Congressional district",
  metadata: { .. },
  name: "4",
  resource_uri: "/1.0/boundary/4-congressional-district/",
  set: "/1.0/boundary-set/congressional-districts/",
  simple_shape: { .. },
  slug: "4-congressional-district"
}
''' # an example JSON response

# Example place
EXAMPLE_PLACE = 'The Minnesota State Capitol'
EXAMPLE_PLACE_LAT_LNG = '44.954155,-93.1038669999999'
EXAMPLE_PLACE_BBOX = '43.499356,-97.239209,49.384358,-89.489226'
EXAMPLE_UNIT = 'kilometre'
EXAMPLE_UNIT_CODE = 'km'

# Analytics
ENABLE_GOOGLE_ANALYTICS = True
GOOGLE_ANALYTICS_KEY = 'UA-3385191-1'

# Code for source page
FORKED_REPO = 'github.com/MinnPost/mn-boundaryservice'
FORKED_REPO_URL = 'https://github.com/MinnPost/mn-boundaryservice'

# About text.  This is inserted as is.
ABOUT_HTML = '''
<p>Minnesota Boundaries is a free service provided by <a href="http://minnpost.com" target="_blank">MinnPost</a> and was developed by <a href="http://minnpost.com/data" target="_blank">MinnPost's interactive team</a>.  The application is based on software created by the <a target="_blank" href="http://blog.apps.chicagotribune.com/">News Applications team</a> at the <a target="_blank" href="http://www.chicagotribune.com">Chicago Tribune</a>.</p>
'''

# Footer text.  This is inserted as is.
FOOTER_HTML = '''
<p style="float:right; text-align: right; width: 50%;">Made by &nbsp;<a href="http://minnpost.com" target="_blank" title="MinnPost homepage"><img src="https://s3.amazonaws.com/data.minnpost/icons/minnpost-logos/logo-150x21.png" alt="MinnPost logo" /></a></p>
'''

try:
    from settings_override import *
except ImportError:
    pass
