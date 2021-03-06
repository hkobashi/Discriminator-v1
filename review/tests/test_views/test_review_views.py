from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from review.views import Review

class NeedlessLoginTests(TestCase):
  def test_get_index(self):
    """
    GETメソッドでアクセスしてステータスコード200を返されることを確認
    """
    response = self.client.get(reverse('review_index'))
    self.assertTemplateUsed(response, "review/index.html")
    self.assertEqual(response.status_code, 200)

  def test_get_detail(self):
    """
    レビュー作成後、詳細ページをGETできるかテスト
    """
    review = Review.objects.create(title='title1', body='body1', storeName='storeName1')
    response = self.client.get(reverse('review_detail', args=(review.id, )))
    self.assertTemplateUsed(response, "review/show.html")
    self.assertEqual(response.status_code, 200)

  def test_review_not_exist(self):
    """
    存在しないレビューは404を返すことテスト
    """
    response_loggedOut = self.client.get(reverse('review_detail', args=(100, )))
    self.assertTemplateUsed(response_loggedOut, "404.html")
    self.assertEqual(response_loggedOut.status_code, 404)

class NeedLoginTests(TestCase):
  def setUp(self):
    """
    ユーザ認証が必要なページを閲覧するためにログイン用ユーザーを作成してログインする
    """
    userModel = get_user_model()
    username = 'testuser'
    email = 'test@com'
    password = 'password'
    userModel.objects.create_user(username, email, password)
    self.client.login(username=username, email=email, password=password)

  def test_get_review_create(self):
    """
    GETメソッドでアクセスすると作成用フォームが返ってくることをテスト
    """
    response_loggedIn = self.client.get(reverse('review_create'))
    self.assertTemplateUsed(response_loggedIn, "review/create.html")
    self.assertEqual(response_loggedIn.status_code, 200)
    # ログインしていないとログインページにリダイレクトされることをテスト
    self.client.logout()
    response_loggedOut = self.client.get(reverse('review_create'))
    self.assertEqual(response_loggedOut.url, "/account/login/?next=/review/create")
    self.assertEqual(response_loggedOut.status_code, 302)

  def test_post_review_create(self):
    """
    POSTメソッドでアクセスするとデータが登録され、review_indexへリダイレクトされていることをテスト
    """
    response_loggedIn = self.client.post(reverse('review_create'), )
    self.assertTemplateUsed(response_loggedIn, "review/create.html")
    self.assertEqual(response_loggedIn.status_code, 200)
    
    # ログインしていないとログインページにリダイレクトされることをテスト
    self.client.logout()
    response_loggedOut = self.client.get(reverse('review_create'))
    self.assertEqual(response_loggedOut.url, "/account/login/?next=/review/create")
    self.assertEqual(response_loggedOut.status_code, 302)


  def test_update_review(self):
    """
    GETメソッドでアクセスすると更新用フォームが返ってくることをテスト
    """
    review = Review.objects.create(title='title1', body='body1', storeName='storeName1')
    response_loggedIn = self.client.get(reverse('review_update', args=(review.id, )))
    self.assertTemplateUsed(response_loggedIn, "review/update.html")
    self.assertEqual(response_loggedIn.status_code, 200)
    
    # ログインしていないとログインページにリダイレクトされることをテスト
    self.client.logout()
    response_loggedOut = self.client.get(reverse('review_update', args=(review.id, )))
    self.assertEqual(response_loggedOut.status_code, 302)

  def test_canNot_update_review(self):
    """
    存在しないレビューの更新ページが返ってこないことをテスト
    """
    response_loggedIn = self.client.get(reverse('review_update', args=(2, )))
    self.assertTemplateNotUsed(response_loggedIn, "review/update.html")
    self.assertEqual(response_loggedIn.status_code, 404)

  def test_delete_review(self):
    """
    作成したレビューが削除できることを確認
    """
    review = Review.objects.create(title='title_delete', body='body_delete', storeName='storeName_delete')
    response_loggedOut = self.client.get(reverse('review_delete', args=(review.id, )))
    self.assertEqual(response_loggedOut.status_code, 302)
    self.assertEqual(response_loggedOut.url, "/review/", msg="review_indexにリダイレクトされていることを確認")