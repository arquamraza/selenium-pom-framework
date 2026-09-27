import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_flipkart_iphone_price():
    print("SDET Bhai Flipkart khol raha hai 🔥")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.flipkart.com")
    time.sleep(3)
    
    # Popup band karne ke liye
    try:
        driver.find_element(By.XPATH, "//button[text()='✕']").click()
    except:
        pass
    
    # iPhone search karo
    driver.find_element(By.NAME, "q").send_keys("iPhone 15" + Keys.ENTER)
    time.sleep(5)
    
    # PROOF LO
    driver.save_screenshot("FLIPKART_IPHONE_PROOF.png")
    print("Screenshot ban gayi: FLIPKART_IPHONE_PROOF.png")
    
    # Ruk jao yahan
    input("Enter dabao to band karu")
    driver.quit()