from selenium import webdriver

import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    browser = webdriver.Chrome(executable_path=r"D:\web_drivers\chromedriver.exe", options=options)
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("//*[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла