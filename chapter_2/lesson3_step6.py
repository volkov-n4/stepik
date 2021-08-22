import math
from selenium import webdriver

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    browser = webdriver.Chrome(executable_path=r"D:\web_drivers\chromedriver.exe", options=options)
    browser.get(link)

    browser.find_element(By.TAG_NAME, 'button').click()

    new = browser.window_handles[1]

    browser.switch_to.window(new)

    x = calc(browser.find_element(By.ID, "input_value").text)

    browser.find_element(By.ID, 'answer').send_keys(x)

    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла