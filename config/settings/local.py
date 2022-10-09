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

# S3接続についての設定
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'kobashikawa-test'
AWS_S3_REGION_NAME = 'ap-northeast-1'

# AWS_ACCESS_KEY_ID = env.get_value('AWS_ACCESS_KEY_ID', str)
# AWS_SECRET_ACCESS_KEY = env.get_value('AWS_SECRET_ACCESS_KEY', str)