from selenium import webdriver
import time

try: 
    link1 = "https://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link1)

    # Ваш код, который заполняет обязательные поля
    element = browser.find_element_by_css_selector("div.first_block input.first")
    element.send_keys("Мой ответ")
    element = browser.find_element_by_css_selector("div.first_block input.second")
    element.send_keys("Мой ответ")
    element = browser.find_element_by_css_selector("div.first_block input.third")
    element.send_keys("Мой ответ")
    
    time.sleep(5)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()