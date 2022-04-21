import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from ex_2.ex2_1 import calc


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.get(link)


def open_wait():
    try:
        WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), text_='100')
        )
        browser.find_element_by_id('book').click()
        x_element = browser.find_element_by_id('input_value')
        x = x_element.text
        y = calc(x)
        inputsend = browser.find_element_by_id('answer')
        inputsend.send_keys(y)
        browser.find_element_by_id('solve').click()

    finally:
        time.sleep(5)
        browser.quit()


if __name__ == "__main__":
    open_wait()