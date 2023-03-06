from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestMultipuleSelect:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://courses.letskodeit.com/practice")
        get_wait = WebDriverWait(self.driver, timeout = 10)

    def test_select_class(self):
        get_wait = WebDriverWait(self.driver, timeout=20)
        select_class = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[id='multiple-select-example']")))
        #select_class.click()

        apple = get_wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[text()='Apple']")))
        assert not apple.is_selected()
        apple.click()

        orange = get_wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[text()='Orange']")))
        assert not orange.is_selected()
        orange.click()

        peach = get_wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[text()='Peach']")))
        assert not peach.is_selected()
        peach.click()



test5 = TestMultipuleSelect()
test5.test_select_class()
#test5.test_apple()