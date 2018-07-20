from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',]

DATABASES = {
    'default': {
			'ENGINE': 'django.contrib.gis.db.backends.postgis',
			'NAME': config('DB_NAME'),
			'USER': config('DB_USER'),
			'PASSWORD': config('DB_PASSWORD'),
			'HOST': config('DB_HOST'),
			'PORT': '',
   		 }
}
