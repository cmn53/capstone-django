from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['rom-free.herokuapp.com',]

DATABASES = {}
DATABASES['default'] =  dj_database_url.config('DATABASE_URL')
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.getenv('GEOS_LIBRARY_PATH')
