from django.db import models

# Create your models here.

class Review(models.Model):
  title = models.CharField(max_length=30)
  body = models.TextField(max_length=100)
  storeName = models.CharField(max_length=30)
#  is_published = models.BooleanField('公開する', default=False, help_text='公開する場合はチェックを入れる')

def __str__(self):
  return "[%s]%s(%s)"%(self.id, self.title, self.body)