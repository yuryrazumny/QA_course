from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time 

def calc(a):
  return str(math.log(abs(12*math.sin(int(a)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_id("book")
    button.click()
    

    x = browser.find_element_by_id("input_value")
    newX = x.text
    y = calc(newX)
    
    answerField = browser.find_element_by_id("answer")
    answerField.send_keys(y)
    
    button = browser.find_element_by_id("solve")

    # Отправляем заполненную форму
    button.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()