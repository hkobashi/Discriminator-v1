from django.forms import ModelForm, fields
from .models import Review

class ReviewForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(ReviewForm, self).__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs["class"] = "form-control"
      
  class Meta:
    model = Review
    fields = ['title', 'body', 'storeName']