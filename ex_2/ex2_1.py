from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


def open1():
    try:
        time.sleep(3)
        x_element = browser.find_element_by_tag_name('img')
        valuex = x_element.get_attribute('valuex')
        # x = valuex.text
        y = calc(valuex)
        inputsend = browser.find_element_by_id('answer')
        inputsend.send_keys(y)

        checkel = browser.find_element_by_id('robotCheckbox')
        checkel.click()

        radioel = browser.find_element_by_id('robotsRule')
        radioel.click()

        submit = browser.find_element_by_tag_name('button')
        submit.click()


    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    open1()
    calc()