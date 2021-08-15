from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    element = browser.find_element_by_name("firstname")
    element.send_keys("Мой ответ")
    element = browser.find_element_by_name("lastname")
    element.send_keys("Мой ответ")
    element = browser.find_element_by_name("email")
    element.send_keys("Мой ответ")

    getFile = browser.find_element_by_id("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           
    # добавляем к этому пути имя файла 
    getFile.send_keys(file_path)
    
    
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