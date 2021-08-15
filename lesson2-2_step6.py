from selenium import webdriver
import time
import math

def calc(a):
  return str(math.log(abs(12*math.sin(int(a)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element_by_id("input_value")
    newX = x.text
    y = calc(newX)
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    answerField = browser.find_element_by_id("answer")
    answerField.send_keys(y)

    getCheckBox = browser.find_element_by_id('robotCheckbox')
    getCheckBox.click()

    getRadioBox = browser.find_element_by_id('robotsRule')
    getRadioBox.click()

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