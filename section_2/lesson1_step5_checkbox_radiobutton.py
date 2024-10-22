from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x_element))

    elements_to_select = tuple(("[id = 'robotCheckbox']", "[id = 'robotsRule']", "button.btn"))
    #browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    #browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    #browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    for elem in elements_to_select:
        browser.find_element(By.CSS_SELECTOR, elem).click()

    time.sleep(1)

    print_answer(browser)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
