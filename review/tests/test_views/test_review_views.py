from django.test import TestCase
from django.urls import reverse

from review.models import Review

class IndexTests(TestCase):
  """IndexViewのテストクラス"""
  def test_get_index(self):
    """
    GET メソッドでアクセスしてステータスコード200を返されることを確認
    """
    response = self.client.get(reverse('review_index'))
    self.assertEqual(response.status_code, 200)