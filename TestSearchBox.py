from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class TestSearchBox:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://courses.letskodeit.com/practice")
        get_wait = WebDriverWait(self.driver, timeout=10)

    def test_auto_suggest(self):
        get_wait = WebDriverWait(self.driver, timeout=20)
        search_box = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[id='autosuggest']")))
        search_box.click()
        search_box.send_keys("auto suggest")

test8 = TestSearchBox()
test8.test_auto_suggest()