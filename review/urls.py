from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="review_index"),
  path('detail/<int:review_id>', views.show, name="review_detail"),
  path('create', views.create, name="review_create"),
  path('update/<int:review_id>', views.update, name="review_update"),
  path('delete/<int:review_id>', views.delete, name="review_delete"),
]