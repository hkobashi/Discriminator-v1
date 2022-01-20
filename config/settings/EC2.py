from .base import *
import environ

# .envにある変数を読み込み
env = environ.Env(DEBUG=(bool,False))
env.read_env(os.path.join(BASE_DIR,'.env'))

SECRET_KEY = env.get_value('SECRET_KEY', str)

DEBUG = env.get_value('DEBUG', bool)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES = {
    'default':env.db(),
}

# SECRET_KEY = '86gi2mhyw(trf-&k3ag*b@)ca7(w_r**zcl^o@us)a0iw7-yv$'


# ALLOWED_HOSTS = ['staging-v1.discriminator.link', '.staging-v1.discriminator.link']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'Discriminator_staging_v1',
#         'USER': 'disc_staging',
#         'PASSWORD': 'CR9BZJ4AP9ZxJ8j',
#         'HOST': 'discriminator-db.cwcfv6dzfauo.ap-northeast-1.rds.amazonaws.com',
#         'PORT': '3306',
#         'TEST': {
#             'NAME': 'test_Discriminator_staging_v1',
#         },
#     }
# }