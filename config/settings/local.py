from .base import *

# INSTALLED_APPS += [
#     "debug_toolbar",
# ]

SECRET_KEY = 'x)-z0gn&$s6(kul_o1b=zkyr6wr7bof2if40rge^tdxsu3hp*q'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Discriminator_dev_v1',
        'USER': 'Disc',
        'PASSWORD': 'V9reamWwANyYc8j',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}