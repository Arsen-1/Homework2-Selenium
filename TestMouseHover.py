from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class TestMouseHover:

    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://courses.letskodeit.com/practice")
        get_wait = WebDriverWait(self.driver, timeout=10)


    def test_mouse_hover(self):
        get_wait = WebDriverWait(self.driver, timeout=10)
        input_name = "Armen"

        mouse_hover = get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="mousehover"]')))
        self.driver.execute_script("arguments[0].scrollIntoView();", mouse_hover)

        self.driver.find_element(By.CSS_SELECTOR, 'input[id="name"]').send_keys(input_name)

        actions = ActionChains(self.driver)
        actions.move_to_element(mouse_hover).perform()

        self.driver.find_element(By.CSS_SELECTOR, 'div[class="mouse-hover-content"] > a:nth-child(2)').click()

        # get_attribute('value') -> returns text in input field
        assert get_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="name"]'))).get_attribute('value') != input_name

test10 = TestMouseHover()
test10.test_mouse_hover()