# Hudl Test
 Repository for test automation
This file contains details of the test script that will be run.

# Prerequisites
- Install Selenium and Pytest
- Download the WebDriver (e.g., ChromeDriver for Google Chrome) and add it to your system PATH.
Replace "your_email@example.com" and "your_password" with valid credentials.
Automation Test Script (HudlLoginTest.py)
python
Copy
Edit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

# Test Data
BASE_URL = "https://www.hudl.com/login"
VALID_EMAIL = "your_email@example.com"
VALID_PASSWORD = "your_password"
INVALID_EMAIL = "invalid_email@example.com"
INVALID_PASSWORD = "wrongpassword"

@pytest.fixture
def driver():
    # Initialize WebDriver
    driver = webdriver.Chrome()  # Ensure ChromeDriver is installed
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    """Test case for valid login"""
    driver.get(BASE_URL)
    
    # Locate elements
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "logIn")
    
    # Perform login
    email_input.send_keys(VALID_EMAIL)
    password_input.send_keys(VALID_PASSWORD)
    login_button.click()
    
    time.sleep(3)  # Wait for page load
    
    # Validate successful login by checking redirected URL or dashboard element
    assert "https://www.hudl.com/home" in driver.current_url, "Login failed!"

def test_invalid_login(driver):
    """Test case for invalid login"""
    driver.get(BASE_URL)
    
    # Locate elements
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "logIn")
    
    # Perform login
    email_input.send_keys(INVALID_EMAIL)
    password_input.send_keys(INVALID_PASSWORD)
    login_button.click()
    
    time.sleep(2)  # Wait for error message
    
    # Check for an error message
    error_message = driver.find_element(By.XPATH, "//p[contains(text(), 'We didn’t recognize that email and/or password.')]")
    assert error_message.is_displayed(), "Error message not displayed!"

if __name__ == "__main__":
    pytest.main(["-v", "HudlLoginTest.py"])
Test Cases Covered
Valid Login: Ensures the user can log in with correct credentials.
Invalid Login: Ensures an error message appears for incorrect credentials.
How to Run the Test
Save the script as HudlLoginTest.py
