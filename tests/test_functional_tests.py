import pytest
from selenium import webdriver


def test_テストが実行できる():
    assert True


def test_Django開発サーバーにアクセスできる():
    browser = webdriver.Chrome()
    browser.get("http://localhost:8000")
    assert "Django" in browser.title
    browser.quit()
