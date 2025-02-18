from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
from dotenv import load_dotenv
import os

HUDL_URL = "https://identity.hudl.com/u/login/password"
# Extracted to a constant for reuse and clarity

# Load environment variables from .env file
load_dotenv()

# Set up the WebDriver (ensure you have the correct driver installed, e.g., chromedriver for Chrome)
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver  # This keeps WebDriver open for the test
    driver.quit()  # Closes WebDriver after test completes

# input("Press Enter to close the browser...")

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
        print(f"Using email: {email[:3]}********@****.com")  # Partial masking

        # Find and fill in the email field
        email_input = driver.find_element(By.ID, "username")
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for transition to the next step

        # Click on "Forgot Password?"
        forgot_password_link = driver.find_element(By.LINK_TEXT, "Forgot Password")
        forgot_password_link.click()
        print("Clicked Forgot Password button")

        # Click continue to send reset email
        submit_button = driver.find_element(By.NAME, "action")
        submit_button.click()
        print("Clicked Continue")

        # Wait for success message
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "container")))
        assert "Check Your Email" in success_message.text, "Check Your Email"
        print("✅ Password reset email sent.")
        time.sleep(2)  # Wait for transition to the next step

        # Ensure the button is clickable
        WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, "action")))

        # Resend email
        WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.NAME, "action")))
        submit_button = driver.find_element(By.NAME, "action")
        submit_button.click()
        print("Clicked Resend Email button")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "container")))

        # Verify user is taken back to Login page
        reset_password_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Reset Password')]")))
        assert "Reset Password" in reset_password_message.text
        print("Test Passed: Forgot password email sent successfully.")

    finally:
        # Ensure the browser is closed even if the test fails
        driver.quit()