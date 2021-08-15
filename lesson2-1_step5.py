from selenium import webdriver
import time
import math

def calc(a):
  return str(math.log(abs(12*math.sin(int(a)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    element = browser.find_element_by_id("input_value")
    x = element.text
    
    y = calc(x)
    
    answerField = browser.find_element_by_id("answer")
    answerField.send_keys(y)

    getCheckBox = browser.find_element_by_id('robotCheckbox')
    getCheckBox.click()

    getRadioBox = browser.find_element_by_id('robotsRule')
    getRadioBox.click()

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