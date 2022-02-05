
from django.forms import BooleanField, CheckboxSelectMultiple, ModelForm, MultipleChoiceField
from .models import Review

class ReviewForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(ReviewForm, self).__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs["class"] = "form-control"
  class Meta:
    model = Review
    fields = ['title', 'body', 'storeName']