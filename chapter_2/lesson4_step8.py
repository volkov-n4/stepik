import math
from selenium import webdriver

import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    browser = webdriver.Chrome(executable_path=r"D:\web_drivers\chromedriver.exe", options=options)
    browser.get(link)

    WebDriverWait(browser, 30).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    browser.find_element(By.ID, 'book').click()

    x = calc(browser.find_element(By.ID, "input_value").text)

    browser.find_element(By.ID, 'answer').send_keys(x)

    browser.find_element(By.ID, 'solve').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла