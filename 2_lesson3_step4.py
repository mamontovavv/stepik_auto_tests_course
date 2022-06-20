from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log((abs(12*math.sin(int(x))))))
try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()


    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    # Посчитать математическую функцию от x
    y = calc(x)

    # Ввести ответ в текстовое поле
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


