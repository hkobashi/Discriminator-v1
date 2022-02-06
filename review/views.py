from django.shortcuts import redirect, render, get_object_or_404
from .models import Review
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

# templates/403.htmlを返す

from .forms import ReviewForm

def index(request):
  review_list = Review.objects.all()
  template = "review/index.html"
  return render(request, template, {'review_list': review_list})

@login_required
def show(request, review_id):
  review = get_object_or_404(Review, pk=review_id)
  template = "review/show.html"
  return render(request, template, {'review': review})
  # if review.is_published:
  #   return render(request, template, {'review': review})
  # else:
  #   raise PermissionDenied

def create(request):
  if request.method == "POST":
    form = ReviewForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('review_index')
  # GETメソッドでReviewForm呼び出し
  form = ReviewForm
  return render(request, "review/create.html", {'form': form})

def update(request, review_id):
  review = get_object_or_404(Review, pk=review_id)
  template = "review/update.html"
  if request.method == "POST":
    form = ReviewForm(request.POST, instance=review)
    if form.is_valid():
      form.save()
      return redirect('review_index')
  form = ReviewForm(instance=review)
  return render(request, template, {'form': form, 'review_id': review_id})

def delete(request, review_id):
  review = get_object_or_404(Review, pk=review_id)
  review.delete()
  return redirect('review_index')