from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (ensure you have the correct driver installed, e.g., chromedriver for Chrome)
driver = webdriver.Chrome()

def test_login_button():
    try:
        # Open the Hudl website
        driver.get("https://www.hudl.com/en_gb/")
        driver.maximize_window()

        # Wait for the page to load
        time.sleep(3)  # Consider using WebDriverWait instead

        # Find the login button and click it and open the dropdown menu
        login_button = driver.find_element(By.LINK_TEXT, "Log in")
        login_button.click()
        time.sleep(3)

        # Find the dropdown menu and click "Hudl"
        hudl_button = driver.find_element(By.LINK_TEXT, "Hudl")  # Replace with actual ID or locator
        hudl_button.click()

        # Wait for navigation
        time.sleep(3)  # Adjust based on actual navigation speed

        # Verify if redirected to the login page
        assert "login" in driver.current_url, "Login button did not navigate correctly"
        print("Test Passed: Login button clicked successfully.")

    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        # Close the browser
        driver.quit()

# Run the test
test_login_button()
