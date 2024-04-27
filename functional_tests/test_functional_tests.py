import pytest
from selenium import webdriver


def test_テストが実行できる():
    assert True


class TestNewVisitorTest:

    def setup_method(self):
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        self.browser.quit()

    # Edith has heard about a cool new online to-do app. She goes
    # to check out its homepage
    def test_can_start_a_list_and_retrieve_it_later(self):

        # She notices the page title and header mention to-do lists
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        assert "To-Do" in self.browser.title
        pytest.fail("Finish the test!")

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)

        # When she hists enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text nox inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        # Edith wonders wether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep
