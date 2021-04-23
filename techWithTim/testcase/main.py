import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\chromedriver.exe")
        self.driver.get("http://www.python.org")

    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matches()

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = 'pycon'
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found()

    def test_example_2(self):
        assert True

    def not_a_test(self):
        print("this won't print")

    def tearDown(self):
        self.driver.close()

if __name__ = "__main__":
    unittest.main()