import math
from selenium import webdriver

import time

from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    browser = webdriver.Chrome(executable_path=r"D:\web_drivers\chromedriver.exe", options=options)
    browser.get(link)

    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys("1")
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys("2")
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('3')

    upload_area = browser.find_element(By.NAME, 'file')
    upload_area.send_keys(r"D:\stepik\stepik\1.txt")

    btn = browser.find_element(By.CLASS_NAME, 'btn')
    btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла