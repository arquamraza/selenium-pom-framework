import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from selenium.webdriver.common.by import By

class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "q")

    def search(self, text):
        self.driver.find_element(*self.search_box).send_keys(text)
        self.driver.find_element(*self.search_box).submit()