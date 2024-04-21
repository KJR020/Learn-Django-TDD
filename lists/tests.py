from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        """
        requestオブジェクトを作成し、home_pageビュー関数に渡す。
        これにより、home_pageのURLを叩いたときに返ってくるレスポンスを取得できる。
        Responseオブジェクトからcontent属性を取得し、その中身を文字列に変換する。
        その文字列が、<html>で始まり、</html>で終わることを確認する。
        """
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf8")
        self.assertIn("<title>To-Do lists</title>", html)
        self.assertTrue(html.startswith("<html>"))
        self.assertTrue(html.endswith("</html>"))
