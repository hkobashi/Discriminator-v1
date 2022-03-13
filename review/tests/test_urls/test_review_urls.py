from django.test import TestCase
from django.urls import reverse, resolve

from review.views import *

class TestUrls(TestCase):
  def test_post_index_url(self):
    """
    index ページへのURLでアクセスする時のリダイレクトをテスト
    """
    url = reverse('review_index')
    self.assertEqual(url, "/review/")
    self.assertEqual(resolve(url).func, index, msg="views.indexが返ってくるかテスト")

  def test_post_list_url(self):
    """
    Post 一覧ページへのリダイレクトをテスト
    リクエストに対して返ってくるviews関数を確認しているため存在しないreview_idでもint型ならテストはパスされる
    """
    url = reverse('review_detail', kwargs={'review_id': 0})
    self.assertEqual(url, "/review/detail/0")
    self.assertEqual(resolve(url).func, show, msg="views.showが返ってくるかテスト")

  def test_elbHealthCheck(self):
    """
    ELBのヘルスチェックをテスト
    """
    url = reverse('elb_healthcheck')
    self.assertEqual(url, "/elbHealthCheck/")