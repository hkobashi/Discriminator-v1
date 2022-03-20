from .base import *
import environ

# .envにある変数を読み込み
env = environ.Env(DEBUG=(bool,False))
env.read_env(os.path.join(BASE_DIR,'.local_env'))

SECRET_KEY = env.get_value('SECRET_KEY', str)

DEBUG = env.get_value('DEBUG', bool)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES = {
    'default':env.db(),
}

MIDDLEWARE += [
    'aws_xray_sdk.ext.django.middleware.XRayMiddleware',
]

INSTALLED_APPS += [
    'aws_xray_sdk.ext.django',
]

XRAY_RECORDER = {
    'AUTO_INSTRUMENT': True,
    'AWS_XRAY_CONTEXT_MISSING': 'LOG_ERROR',
    'AWS_XRAY_DAEMON_ADDRESS': '127.0.0.1:2000',
    'AWS_XRAY_TRACING_NAME': 'Discriminator-local',
    'SAMPLING': False,
}

# 画像保存先URLを指定
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')