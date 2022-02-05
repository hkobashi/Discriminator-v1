from django.contrib import admin
from .models import Review

class Review_admin(admin.ModelAdmin):
  list_display = ['title', 'is_published']

admin.site.register(Review, Review_admin)