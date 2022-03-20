from django.shortcuts import redirect, render, get_object_or_404
from .models import Review
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .forms import ReviewForm

def index(request):
  review_list = Review.objects.all()
  template = "review/index.html"
  # 検索機能
  keyword = request.GET.get('keyword')
  if keyword:
    result = review_list.filter(
      # タイトル、本文で検索
      Q(title__icontains=keyword) |
      Q(body__icontains=keyword)
    )
    messages.success(request, '「{}」の検索結果'.format(keyword))
    # 検索にヒットしたもののみ表示
    return render(request, template, {'review_list': result})

  return render(request, template, {'review_list': review_list})

def show(request, review_id):
  review = get_object_or_404(Review, pk=review_id)
  user = review.user
  template = "review/show.html"
  return render(request, template, {'review': review})

@login_required
def create(request):
  if request.method == "POST":
    copied = request.POST.copy()
    copied["user"] = request.user.id
    form = ReviewForm(copied)
    if form.is_valid():
      form.save()
      return redirect('review_index')
  # GETメソッドでReviewForm呼び出し
  form = ReviewForm
  return render(request, "review/create.html", {'form': form})

@login_required
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

@login_required
def delete(request, review_id):
  review = get_object_or_404(Review, pk=review_id)
  review.delete()
  return redirect('review_index')