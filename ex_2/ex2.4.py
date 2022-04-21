from selenium import webdriver
import time
import os


link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)


def fileos():
    try:
        time.sleep(1)
        browser.find_element_by_name('firstname').send_keys('Aly')
        browser.find_element_by_name('lastname').send_keys('Gordon')
        browser.find_element_by_name('email').send_keys('qwer@qwer.ru')
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'test.txt')
        browser.find_element_by_id('file').send_keys(file_path)
        button = browser.find_element_by_class_name('btn')
        button.click()

    finally:
        time.sleep(5)
        browser.quit()


fileos()