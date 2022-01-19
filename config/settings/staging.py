from .base import *

SECRET_KEY = 'django-insecure-86gi2mhyw(trf-&k3ag*b@)ca7(w_r**zcl^o@us)a0iw7-yv$'


ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Discriminator_staging_v1',
        'USER': 'disc_staging',
        'PASSWORD': 'GKGa0C04fqjNZDAbbaKb',
        'HOST': 'discriminator-db.cwcfv6dzfauo.ap-northeast-1.rds.amazonaws.com',
        'PORT': '3306',
        'TEST': {
            'NAME': 'test_Discriminator_staging_v1',
        },
    }
}

