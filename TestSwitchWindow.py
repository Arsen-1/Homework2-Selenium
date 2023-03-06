from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestSwitchWindow:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://courses.letskodeit.com/practice")
        get_wait = WebDriverWait(self.driver, timeout = 10)

    def test_switch_window(self):
      get_wait = WebDriverWait(self.driver, timeout=20)
      switch_window = get_wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[text()='Open Window']")))
      switch_window.click()
      button = get_wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "//*[text()='Sign In']")))
      #self.driver.switch_to.window("switch_window")
      button.click()
      self.driver.switch_to.window("[class='overly']")
test3 = TestSwitchWindow()
test3.test_switch_window()