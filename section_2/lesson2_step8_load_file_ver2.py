import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    last_name = browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    email = browser.find_element(By.NAME, "email").send_keys("test_email")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла

    with open("test.txt", "w") as file:
        content = file.write("TestingText")  # create test.txt file

    file_path = os.path.join(current_dir, "test.txt")
    load_file = browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)
    submit_button = browser.find_element(By.CLASS_NAME, "btn").click()

    print_answer(browser)

finally:
    os.remove(file_path)  # удаляем наш файл из каталога
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()
