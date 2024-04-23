from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        """
        clientオブジェクトを使って、home_pageビュー関数にリクエストを送信し、レスポンスを取得する
        responseオブジェクトのcontent属性を使わずに、assertContainsメソッドを使用
        """
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")
