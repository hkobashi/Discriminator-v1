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