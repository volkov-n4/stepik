import unittest

from selenium import webdriver

from selenium.webdriver.common.by import By


class TestRun(unittest.TestCase):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.browser = webdriver.Chrome(executable_path=r"D:\web_drivers\chromedriver.exe")

    def get_page(self, link):
        self.browser.get(link)

    def send_submit(self):
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

    def fill_fields(self):
        first_name = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        first_name.send_keys("Vadim")

        last_name = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        last_name.send_keys("Vadim")

        last_name = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        last_name.send_keys("Vadim")

    def find_answer(self):
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        return welcome_text


    def test_first_page(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.get_page(link)
        self.fill_fields()
        self.send_submit()
        welcome_text = self.find_answer()
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_second_page(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.get_page(link)
        self.fill_fields()
        self.send_submit()
        welcome_text = self.find_answer()

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()