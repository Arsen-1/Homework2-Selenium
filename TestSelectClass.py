from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestSelectClass:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://courses.letskodeit.com/practice")
        get_wait = WebDriverWait(self.driver, timeout = 10)

    def test_select_class(self):
        get_wait = WebDriverWait(self.driver, timeout=20)
        select_class = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[id='carselect']")))
        select_class.click()

        bmw = get_wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[text()='BMW']")))
        assert bmw.is_selected()
        bmw.click()

        benz = get_wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[text()='Benz']")))
        assert not benz.is_selected()
        benz.click()

        honda = get_wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[text()='Honda']")))
        assert not honda.is_selected()
        honda.click()




test4 = TestSelectClass()
test4.test_select_class()
