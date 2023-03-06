from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCheckBox:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://courses.letskodeit.com/practice")
        get_wait = WebDriverWait(self.driver, timeout=10)


        bmw_checkbox = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='bmwcheck']")))
        benz_checkbox = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='benzcheck']")))
        honda_checkbox = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='hondacheck']")))


    def test_checkbox_buttons(self):
        get_wait = WebDriverWait(self.driver, timeout=10)
        bmw_checkbox = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='bmwcheck']")))
        assert not bmw_checkbox.is_selected()
        bmw_checkbox.click()
        bmw_checkbox.click()
        benz_checkbox = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='benzcheck']")))
        assert not benz_checkbox.is_selected()
        benz_checkbox.click()
        benz_checkbox.click()
        honda_checkbox = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='hondacheck']")))
        assert not honda_checkbox.is_selected()
        honda_checkbox.click()
        honda_checkbox.click()

    def test_BMW(self):
        get_wait = WebDriverWait(self.driver, timeout=10)
        bmw_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='bmwcheck']")))
        bmw_radiobutton.click()
        assert bmw_radiobutton.is_selected()
        bmw_radiobutton.click()
        benz_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='benzcheck']")))
        assert not benz_radiobutton.is_selected()
        honda_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='hondacheck']")))
        assert not honda_radiobutton.is_selected()


    def test_benz(self):
        get_wait = WebDriverWait(self.driver, timeout=10)
        benz_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='benzcheck']")))
        benz_radiobutton.click()
        assert benz_radiobutton.is_selected()
        benz_radiobutton.click()
        bmw_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='bmwcheck']")))
        assert not bmw_radiobutton.is_selected()
        honda_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='hondacheck']")))
        assert not honda_radiobutton.is_selected()


    def test_honda(self):
        get_wait = WebDriverWait(self.driver, timeout=10)
        honda_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='hondacheck']")))
        honda_radiobutton.click()
        assert honda_radiobutton.is_selected()
        honda_radiobutton.click()
        benz_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='benzcheck']")))
        assert not benz_radiobutton.is_selected()
        bmw_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='bmwcheck']")))
        assert not bmw_radiobutton.is_selected()


    def test_BMW_benz(self):
        get_wait = WebDriverWait(self.driver, timeout=10)
        bmw_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='bmwcheck']")))
        bmw_radiobutton.click()
        assert bmw_radiobutton.is_selected()
        bmw_radiobutton.click()
        benz_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='benzcheck']")))
        benz_radiobutton.click()
        assert benz_radiobutton.is_selected()
        benz_radiobutton.click()
        honda_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='hondacheck']")))
        assert not honda_radiobutton.is_selected()


    def test_benz_honda(self):
        get_wait = WebDriverWait(self.driver, timeout=10)
        benz_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='benzcheck']")))
        benz_radiobutton.click()
        assert benz_radiobutton.is_selected()
        benz_radiobutton.click()
        honda_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='hondacheck']")))
        honda_radiobutton.click()
        assert honda_radiobutton.is_selected()
        honda_radiobutton.click()
        bmw_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='bmwcheck']")))
        assert not bmw_radiobutton.is_selected()



    def test_honda_bmw(self):
        get_wait = WebDriverWait(self.driver, timeout=10)
        honda_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='hondacheck']")))
        honda_radiobutton.click()
        assert honda_radiobutton.is_selected()
        honda_radiobutton.click()
        bmw_radiobutton = get_wait.until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='bmwcheck']")))
        bmw_radiobutton.click()
        assert bmw_radiobutton.is_selected()
        bmw_radiobutton.click()
        benz_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='benzcheck']")))
        assert not benz_radiobutton.is_selected()

    def test_honda_bmw_benz(self):
        get_wait = WebDriverWait(self.driver, timeout=10)
        honda_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='hondacheck']")))
        honda_radiobutton.click()
        assert honda_radiobutton.is_selected()
        honda_radiobutton.click()
        bmw_radiobutton = get_wait.until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='bmwcheck']")))
        bmw_radiobutton.click()
        assert bmw_radiobutton.is_selected()
        bmw_radiobutton.click()
        benz_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[id='benzcheck']")))
        benz_radiobutton.click()
        assert benz_radiobutton.is_selected()
        benz_radiobutton.click()

test2 = TestCheckBox()
test2.test_checkbox_buttons()
test2.test_BMW()
test2.test_benz()
test2.test_honda()
test2.test_benz_honda()
test2.test_BMW_benz()
test2.test_honda_bmw()
test2.test_honda_bmw_benz()