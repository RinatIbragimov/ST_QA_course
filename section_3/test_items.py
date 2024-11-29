import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
import time


def test_search_button_add_to_card(browser):

    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    browser.get(link)
    time.sleep(30)

    try:
        #Пытаемся найти кнопку "Добавить в корзину"
        assert browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form>button.btn')
        print('Кнопка "Добавить в корзину" присутствует')

    except NoSuchElementException:
        # Если кнопки "Добавить в корзину" нет
        print('Кнопка "Добавить в корзину" отсутствует')

    finally:
        print("Тест завершен")
