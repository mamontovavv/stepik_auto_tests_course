from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log((abs(12*math.sin(int(x))))))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд и цена 100
    WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,'price'),"$100"))

    button1 = browser.find_element(By.CSS_SELECTOR, '#book')
    button1.click()

    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    # Посчитать математическую функцию от x
    y = calc(x)

    # Ввести ответ в текстовое поле
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer) 
    answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


