from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class DisableEnable:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://courses.letskodeit.com/practice")
        get_wait = WebDriverWait(self.driver, timeout=10)

    def disable_enable(self):
        get_wait = WebDriverWait(self.driver, timeout=20)
        disable_enable = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[id='enabled-example-input']")))

        disable = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[id='disabled-button']")))
        disable.click()
        assert not disable_enable.is_enabled()
        #disable_enable.send_keys("test1")
        enable = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[id='enabled-button']")))
        enable.click()
        assert disable_enable.is_enabled()
        disable_enable.send_keys("test2")

test6 = DisableEnable()
test6.disable_enable()