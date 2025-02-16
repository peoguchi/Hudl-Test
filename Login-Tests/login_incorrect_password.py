from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
from dotenv import load_dotenv
import os

HUDL_URL = "https://www.hudl.com/en_gb/"
# Extracted to a constant for reuse and clarity

# Load environment variables from .env file
load_dotenv()

# Ensure HUDL_PASSWORD_2 is retrieved correctly
password2 = os.getenv("HUDL_PASSWORD_2")

# Debugging - Check if password2 is retrieved correctly
if not password2:
    raise ValueError("ERROR: HUDL_PASSWORD_2 is missing or not loading from .env file!")

print(f"Debug: Retrieved password2 = {'*' * len(password2)}")  # Masked output


# Set up the WebDriver (ensure you have the correct driver installed, e.g., chromedriver for Chrome)
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver  # This keeps WebDriver open for the test
    driver.quit()  # Closes WebDriver after test completes

def test_login_button(driver):
    driver.get(HUDL_URL)
    try:
        # Open the Hudl website
        driver.get(HUDL_URL)
        print("Opened Hudl homepage")
        driver.maximize_window()

        # Wait for the page to load
        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Log in")))
        print("Clicked login button")
        # time.sleep(5)  # Consider using WebDriverWait instead

        # Find the login button and click it to open the dropdown menu
        login_button = driver.find_element(By.LINK_TEXT, "Log in")
        login_button.click()
        print("Navigated to Hudl login page")
        time.sleep(3)

        # Find the dropdown menu and click "Hudl"
        hudl_button = driver.find_element(By.LINK_TEXT, "Hudl")  # Replace with actual ID or locator
        hudl_button.click()
        print("Clicked subnav button")

        # Wait for navigation
        time.sleep(3)  # Adjust based on actual navigation speed

        # Get email from environment variables
        email = os.getenv("HUDL_EMAIL")
        print(f"Using email: {email[:3]}********@****.***")  # Partial masking

        # Find and fill in the email field
        email_input = driver.find_element(By.ID, "username")
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for transition to the next step

        # Locate the Password field
        password2_input = driver.find_element(By.ID, "password")

        # Enter incorrect password
        password2_input.clear()  # Clear the field first (optional but recommended)
        password2_input.send_keys(password2)  # Uses "HUDL_PASSWORD_2" from .env
        print("Entered password (masked)")

        # Submit form
        password2_input.send_keys(Keys.RETURN)
        time.sleep(5)  # Wait for login to complete

        # Verify password validation error is shown
        error_message = driver.find_element(By.CLASS_NAME, "ulp-input-error-message").text
        if "email or password is incorrect" in error_message:
            print("Login failed: Incorrect email or password. Test Successful.")
        else:
            print("Unknown login error. Please check test manually to verify:", error_message)
    except NoSuchElementException:
        # If no error message is found, assume test failed
        print("Error: NoSuchElementException occurred. Test failed.")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()


# Run the test (uncomment below if running directly as a script)
# test_login_button()
