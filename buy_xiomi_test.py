from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains


search_button_selector = (By.ID, 'Menu_B2C_Search')

def test_xiomi(driver: Chrome):
    driver.find_element(*search_button_selector).click()

