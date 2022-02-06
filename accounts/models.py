from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

class CustomUserManager(UserManager):
  use_in_migrations = True

  def _create_user(self, email, username, password, **extra_fields):
    if not email:
      raise ValueError('emailを記入してください')
    if not username:
      raise ValueError('ユーザー名を記入してください')
    
    user = self.model(email=email, username=username, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, username, email=None, password=None, **extra_fields):
    if not email:
      raise ValueError('emailを記入してください')
    if not username:
      raise ValueError('ユーザー名を記入してください')
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, username, password, **extra_fields)

  def create_superuser(self, username, email=None, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff')is not True:
      raise ValueError('スタッフ権限がありません')
    if extra_fields.get('is_superuser')is not True:
      raise ValueError('管理者権限がありません')

    return self._create_user(email, username, password, **extra_fields)

class CustomUser(AbstractUser):
  objects = CustomUserManager()

  def __str__(self):
    return self.email