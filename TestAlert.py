from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class TestAlert:

    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://courses.letskodeit.com/practice")
        get_wait = WebDriverWait(self.driver, timeout=10)


    def test_alert(self):

        #name = "Arsen"
        get_wait = WebDriverWait(self.driver, timeout=10)
        #name_button = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[id='name']")))
        #name_button.send_keys(name)

        #alert_button = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[id='alertbtn']")))
        #alert_button.click()
        #alert = self.driver.switch_to.alert
        #assert alert.text == f'Hello {name}, share this practice page and share your knowledge'
        #alert.accept()

        first_name = "Levon"
        second_name = "Hayk"

        alert = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="name"]')))
        alert.send_keys(first_name)

        self.driver.find_element(By.CSS_SELECTOR, 'input[id="alertbtn"]').click()
        first_alert = self.driver.switch_to.alert

        assert first_alert.text == f'Hello {first_name}, share this practice page and share your knowledge'
        first_alert.accept()

        alert.send_keys(second_name)
        self.driver.find_element(By.CSS_SELECTOR, 'input[id="confirmbtn"]').click()

        second_alert = self.driver.switch_to.alert

        assert second_alert.text == f'Hello {second_name}, Are you sure you want to confirm?'
        second_alert.dismiss()

test9 = TestAlert()
test9.test_alert()
