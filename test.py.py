from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Arquam SDET ban gaya")
search_box.submit()

print("Bhai Search bhi ho gaya! Ab job pakki 👑")
time.sleep(5)
driver.quit()