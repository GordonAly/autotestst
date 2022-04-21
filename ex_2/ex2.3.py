from selenium import webdriver
import time
import math
#from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)


def open1():
    try:
        time.sleep(1)
        x_element = browser.find_element_by_id('input_value')
        x = x_element.text
        y = calc(x)
        inputsend = browser.find_element_by_id('answer')
        inputsend.send_keys(y)
        browser.find_element_by_id('robotCheckbox').click()
        browser.execute_script('window.scrollBy(0,100);')
        browser.find_element_by_id('robotsRule').click()
        button = browser.find_elements_by_tag_name('button')
        button[0].click()


    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


open1()