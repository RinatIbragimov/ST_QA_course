from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #num_1 = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    #num_2 = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    sum = int(browser.find_element(By.CSS_SELECTOR, "#num1").text) + int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    #print(sum)

    Select(browser.find_element(By.ID, "dropdown")).select_by_value(str(sum))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(2)
    print_answer(browser)
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()
