from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")

    # Создаем строку из букв англ.алфавита в нижнем регистре
    letters = string.ascii_lowercase
    # print(letters)


    for element in elements:
        # В цикл добавляем генерацию случайного набора символов(диапазон произвольный)
        random_word = ''.join(random.choice(letters) for _ in range(8))
        # По соглашению _ означает для других разработчиков, что переменная не используется
        # Заполняем наше поле этим словом
        element.send_keys(random_word)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
