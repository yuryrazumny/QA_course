from selenium import webdriver
import time
import math

def calc(a):
  return str(math.log(abs(12*math.sin(int(a)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    button = browser.find_element_by_tag_name("button")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_id("input_value")
    newX = x.text
    y = calc(newX)
    
    answerField = browser.find_element_by_id("answer")
    answerField.send_keys(y)
    
    button = browser.find_element_by_tag_name("button")

    # Отправляем заполненную форму
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()