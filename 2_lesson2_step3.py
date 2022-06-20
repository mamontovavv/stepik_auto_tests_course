from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def sum(x, y):
    return str(int(x) + int(y))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
 
    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, '#num1')
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, '#num2')
    y = y_element.text
 

    # Выбираем в выпадающем списке значение равное нашей сумме
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum(x, y))

    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

