from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class ShowHide:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://courses.letskodeit.com/practice")
        get_wait = WebDriverWait(self.driver, timeout=10)

    def show_hide(self):
        get_wait = WebDriverWait(self.driver, timeout=10)
        show_hide_button = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[id='displayed-text']")))
        show_hide_button.click()
        assert show_hide_button.is_displayed()

        hide_button = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='hide-textbox']")))
        hide_button.click()
        assert not show_hide_button.is_displayed()

        show_button = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='show-textbox']")))
        show_button.click()
        assert show_hide_button.is_displayed()


test7 = ShowHide()
test7.show_hide()
