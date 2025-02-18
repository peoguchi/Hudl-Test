from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

HUDL_URL = "https://identity.hudl.com/u/login/password"
TEMPMAIL_URL = "https://tempmailo.com/"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


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
    except Exception as e:
        print(f"An error occurred: {e}")

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

    # Open tempmail and get reset link
    driver.get(TEMPMAIL_URL)
    time.sleep(5)  # Allow email to arrive

    # consent to cookies
# def test_cookie_consent(driver):
    # driver.get("https://tempmailo.com/")

    try:
        consent_button = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'fc-button-label')]"))
        )
        driver.execute_script("arguments[0].click();", consent_button)
        print("✅ Cookie consent accepted")
    except Exception as e:
        print(f"❌ Consent button not found: {e}")

    # Click on the first email
    email_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.mail")))
    email_element.click()

    # Find the reset link inside email
    reset_link_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'reset-password')]")))
    reset_link = reset_link_element.get_attribute("href")
    print(f"Found reset link: {reset_link}")

    # Open reset link
    driver.get(reset_link)

    # Enter new password
    new_password = "NewSecureP@ssword123"
    password_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    confirm_password_input = driver.find_element(By.ID, "confirm-password")

    password_input.send_keys(new_password)
    confirm_password_input.send_keys(new_password)
    confirm_password_input.send_keys(Keys.RETURN)

    print("Password successfully reset")

    # Verify success message
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Password Reset Successful')]"))
    )
    assert "Password Reset Successful" in success_message.text
