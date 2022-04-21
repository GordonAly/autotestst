from selenium import webdriver
import time
#from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)


def open1():
    try:
        time.sleep(1)
        num1 = browser.find_element_by_id('num1')
        num1el = num1.text
        num2 = browser.find_element_by_id('num2')
        num2el = num2.text
        sumselector = int(num1el) + int(num2el)
        print(sumselector)
        select = browser.find_elements_by_tag_name('select')
        select[0].click()
        browser.find_element_by_css_selector(f'[value = "{sumselector}"]').click()
        button = browser.find_elements_by_tag_name('button')
        button[0].click()


    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


open1()