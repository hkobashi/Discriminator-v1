from django.test import TestCase
from review.forms import ReviewForm
from review.models import Review
from django.contrib.auth import get_user_model



class ReviewCreateFormsTests(TestCase):
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

  def test_create_review_with_form(self):
    """
    POSTメソッドで正しいデータを入れるとバリデーションが通ることをテスト
    """
    
    data = {
      "title": "form_test_title",
      "body": "form_test_body",
      "storeName": "form_test_storeName",
    }
    form = ReviewForm(data)
    self.assertTrue(form.is_valid())

    result = self.client.post(path='/review/create', data=data)
    self.assertEqual(result.status_code, 302)
    self.assertEqual(result.url, "/review/",  msg="review_indexにリダイレクトされていることを確認")

  def test_title_validation(self):
    """
    タイトルが空だとバリデーションが通らないことをテスト
    """
    data = {
      "title": "",
      "body": "form_test_body",
      "storeName": "form_test_storeName",
    }
    form = ReviewForm(data)
    self.assertFalse(form.is_valid())

  def test_body_validation(self):
    """
    本文が空だとバリデーションが通らないことをテスト
    """
    data = {
      "title": "form_test_title",
      "body": "",
      "storeName": "form_test_storeName",
    }
    form = ReviewForm(data)
    self.assertFalse(form.is_valid())

  def test_storeName_validation(self):
    """
    店名が空だとバリデーションが通らないことをテスト
    """
    data = {
      "title": "form_test_title",
      "body": "form_test_body",
      "storeName": "",
    }
    form = ReviewForm(data)
    self.assertFalse(form.is_valid())

class ReviewUpdateFormsTests(TestCase):
  def test_post_review_with_form(self):
    """
    POSTメソッドで正しいデータを入れるとバリデーションが通ることをテスト
    """
    pass

  def test_title_validation(self):
    """
    タイトルが空だとバリデーションが通らないことをテスト
    """
    data = {
      "title": "",
      "body": "form_test_body",
      "storeName": "form_test_storeName",
    }
    form = ReviewForm(data)
    self.assertFalse(form.is_valid())

  def test_body_validation(self):
    """
    本文が空だとバリデーションが通らないことをテスト
    """
    data = {
      "title": "form_test_title",
      "body": "",
      "storeName": "form_test_storeName",
    }
    form = ReviewForm(data)
    self.assertFalse(form.is_valid())

  def test_storeName_validation(self):
    """
    店名が空だとバリデーションが通らないことをテスト
    """
    data = {
      "title": "form_test_title",
      "body": "form_test_body",
      "storeName": "",
    }
    form = ReviewForm(data)
    self.assertFalse(form.is_valid())