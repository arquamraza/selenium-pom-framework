import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def test_google_search():
    print("SDET Bhai Google khol raha hai 🔥")
    
    # seedha Chrome kholega bina download ke
    driver = webdriver.Chrome()
    
    driver.get("https://www.google.com")
    driver.maximize_window()
    
    print("Google khul gaya bhai")
    time.sleep(3)
    
    driver.quit()
    print("Test khatam")

if __name__ == "__main__":
    test_google_search()