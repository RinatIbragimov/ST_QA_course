from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#проверяем значение атрибута checked у people_radio
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked) #True
    assert people_checked is not None, "People radio is not selected by default" #True

#проверяем значение атрибута checked у robots_radio
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots_radio: ", robots_checked) # None
    assert robots_checked is None #True

#проверяем значение атрибута disabled у кнопки Submit (кнопка прожимается)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit: ", button_disabled) #None
    assert button_disabled is None #True

#проверяем значение атрибута disabled у кнопки Submit после таймаута (кнопка не прожимается)
    time.sleep(10)
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit after 10sec: ", button_disabled) #True
    assert button_disabled is not None #False

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
