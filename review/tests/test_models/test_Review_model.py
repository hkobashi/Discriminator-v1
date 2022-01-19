from django.test import TestCase
from review.models import Review

class ReviewModelTests(TestCase):
  def test_is_empty(self):
    """
    初期状態では何も登録されていないことをチェック
    """
    saved_Reviews = Review.objects.all()
    self.assertEqual(saved_Reviews.count(), 0)

  def test_is_count_one(self):
    """
    1つレコードを適当に作成すると、レコードが1つだけカウントされることをテスト
    """
    review = Review(title='test_title', body='test_body', storeName='test_storeName')
    review.save()
    saved_Reviews = Review.objects.all()
    self.assertEqual(saved_Reviews.count(), 1)

  def test_saving_and_retrieving_Review(self):
    """
    内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト
    """
    review = Review()
    title = 'test_title_to_retrieve'
    body = 'test_body_to_retrieve'
    storeName='test_storeName_to_retrieve'
    review.title = title
    review.body = body
    review.storeName = storeName
    review.save()

    saved_Reviews = Review.objects.all()
    actual_Review = saved_Reviews[0]

    self.assertEqual(actual_Review.title, title)
    self.assertEqual(actual_Review.body, body)
    self.assertEqual(actual_Review.storeName, storeName)

