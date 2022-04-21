from selenium import webdriver
import time
from ex2_1 import calc



link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)


def window_open():
    try:
        time.sleep(1)
        browser.find_element_by_tag_name('button').click()
        confirm = browser.switch_to_alert()
        confirm.accept()
        x_element = browser.find_element_by_id('input_value')
        x = x_element.text
        y = calc(x)
        inputsend = browser.find_element_by_id('answer')
        inputsend.send_keys(y)
        browser.find_element_by_class_name('btn ').click()

    finally:
        time.sleep(5)
        browser.quit()



if __name__ == "__main__":
    window_open()