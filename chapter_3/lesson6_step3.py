import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def answer():
    return str(math.log(int(time.time())))


@pytest.mark.parametrize('url', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"])
def test_find_message(browser: webdriver.Chrome, url):
    browser.get(url)

    # Find input area
    input_area = WebDriverWait(browser, 30).\
        until(EC.element_to_be_clickable((By.TAG_NAME, 'textarea')))
    input_area.send_keys(answer())

    # Press submit
    btn = browser.find_element(By.CLASS_NAME, 'submit-submission')
    btn.click()

    # Check extend feedback
    feedback = WebDriverWait(browser, 30).\
        until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.attempt__message > div'))).text

    assert "Correct!" == feedback