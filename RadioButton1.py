from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class TestRadioButton:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://courses.letskodeit.com/practice')
        get_wait = WebDriverWait(self.driver, timeout=10)

        bmw_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="bmwradio"]')))
        benz_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="benzradio"]')))
        honda_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="hondaradio"]')))

    def test_radio_buttons_buttons(self):
        get_wait = WebDriverWait(self.driver, timeout=10)

        bmw_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable(( By.CSS_SELECTOR, 'input[id="bmwradio"]')))
        assert not bmw_radiobutton.is_selected()
        bmw_radiobutton.click()
        #status = self.driver.find_element(By.XPATH, "//input[@id='bmwradio']").is_selected()
        #print(status)
        #status = self.driver.find_element(By.XPATH, "//input[@id='bmwradio']").is_selected()
        #print(status)
        #assert not bmw_radiobutton.is_selected()
        benz_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="benzradio"]')))
        assert not benz_radiobutton.is_selected()
        benz_radiobutton.click()

        honda_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="hondaradio"]')))
        assert not honda_radiobutton.is_selected()
        honda_radiobutton.click()

    def test_BMW(self):
        get_wait = WebDriverWait(self.driver, timeout=10)
        bmw_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="bmwradio"]')))
        bmw_radiobutton.click()
        assert bmw_radiobutton.is_selected()
        benz_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="benzradio"]')))
        assert not benz_radiobutton.is_selected()
        honda_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="hondaradio"]')))
        assert not honda_radiobutton.is_selected()


    def test_benz(self):
        get_wait = WebDriverWait(self.driver, timeout = 10)
        benz_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="benzradio"]')))
        benz_radiobutton.click()
        assert benz_radiobutton.is_selected()
        bmw_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="bmwradio"]')))
        assert not bmw_radiobutton.is_selected()
        honda_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="hondaradio"]')))
        assert not honda_radiobutton.is_selected()


    def test_honda(self):
        get_wait = WebDriverWait(self.driver, timeout = 10)
        honda_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="hondaradio"]')))
        honda_radiobutton.click()
        assert honda_radiobutton.is_selected()
        benz_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="benzradio"]')))
        assert not benz_radiobutton.is_selected()
        bmw_radiobutton = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="bmwradio"]')))
        assert not bmw_radiobutton.is_selected()



test1 = TestRadioButton()
#test2 = TestCheckBox()
test1.test_radio_buttons_buttons()
test1.test_BMW()
test1.test_benz()
test1.test_honda()
#test2.test_checkbox_buttons()