from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from random import choice
import string

def GenRandomLine(length=5, chars=string.ascii_lowercase + string.digits):
    return ''.join([choice(chars) for i in range(length)])

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    [element.send_keys(GenRandomLine()) for element in browser.find_elements(By.CSS_SELECTOR, "[required]")]
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

except Exception as e:
    print(e)

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
