from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

def login_hudl():
    # Set up the WebDriver (Make sure you have chromedriver installed)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode if using in GitHub Actions
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://www.hudl.com/login")
        time.sleep(2)  # Wait for the page to load
        
        # Find and fill in the username field
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys(os.getenv("HUDL_EMAIL"))
        
        # Find and fill in the password field
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(os.getenv("HUDL_PASSWORD"))
        
        # Submit the login form
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)  # Wait for login to process
        
        # Verify login success
        if "dashboard" in driver.current_url:
            print("Login successful!")
        else:
            print("Login failed!")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    login_hudl()
