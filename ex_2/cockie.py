from selenium import webdriver


link = "https://lenta.com"
browser = webdriver.Chrome()
browser.get(link)

# Перейти на необходимый домен

# Установить куки. Следующий cookie действителен для всего домена
cookie = {"ключ": "значение"}
browser.add_cookie(cookie)

# И теперь получим все доступные куки для текущего адреса URL
all_cookies = browser.get_cookies()
for cookie_name, cookie_value in all_cookies.items():
    print("%s -> %s", cookie_name, cookie_value)

