def test_flipkart_search(driver):
    driver.get("https://www.google.com")
    print("Title is:", driver.title)
    assert "Google" in driver.title