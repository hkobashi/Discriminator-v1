from django.db import models
from django.contrib.auth import get_user_model

class Review(models.Model):
  title = models.CharField(max_length=30, verbose_name="タイトル")
  body = models.TextField(max_length=100, verbose_name="レビュー")
  storeName = models.CharField(max_length=30, verbose_name="店名")

  user = models.ForeignKey(
    get_user_model(),
    verbose_name="投稿者",
    on_delete=models.CASCADE, 
    null=True,
    blank=True
  )

def __str__(self):
  return "[%s]%s(%s)"%(self.id, self.title, self.body)