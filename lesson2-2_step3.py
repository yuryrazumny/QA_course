from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    xElement = browser.find_element_by_id("num1")
    xElement = xElement.text
    yElement = browser.find_element_by_id("num2")
    yElement = yElement.text

    y = int(xElement) + int(yElement)

    browser.find_element_by_tag_name("select").click()
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(y))
    browser.find_element_by_tag_name("select").click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()