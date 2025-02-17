from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import os
import imaplib
import email
import re
from dotenv import load_dotenv

# Load environment variables (Ensure .env file has EMAIL, PASSWORD)
load_dotenv()

HUDL_URL = "https://identity.hudl.com/u/login/password"
EMAIL = os.getenv("HUDL_EMAIL")
EMAIL_PASSWORD = os.getenv("HUDL_EMAIL_PASSWORD")  # Ensure App Password if using Gmail
IMAP_SERVER = "imap.gmail.com"  # Change based on email provider

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def fetch_reset_link():
    """Fetches the password reset link from the email using IMAP."""
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, EMAIL_PASSWORD)
    mail.select("inbox")

    # Search for the password reset email (change search criteria if needed)
    result, data = mail.search(None, 'UNSEEN FROM "no-reply@hudl.com" SUBJECT "Reset Your Password"')

    if not data[0]:
        raise Exception("No password reset email found.")

    email_ids = data[0].split()
    latest_email_id = email_ids[-1]

    # Fetch the email content
    result, email_data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = email_data[0][1].decode("utf-8")
    msg = email.message_from_string(raw_email)

    # Extract the reset link using regex
    reset_link = None
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True).decode()
            match = re.search(r"https://identity\.hudl\.com/reset-password[^\s]+", body)
            if match:
                reset_link = match.group(0)
                break

    mail.logout()

    if not reset_link:
        raise Exception("Reset link not found in email.")

    return reset_link

def test_reset_password_flow(driver):
    """End-to-end test for resetting password"""
    driver.get(HUDL_URL)

    # Click 'Forgot Password'
    forgot_password_link = driver.find_element(By.LINK_TEXT, "Forgot Password")
    forgot_password_link.click()
    print("Clicked 'Forgot Password'.")

    # Enter email
    email_input = driver.find_element(By.ID, "email-input")
    email_input.send_keys(EMAIL)

    # Submit request
    submit_button = driver.find_element(By.NAME, "action")
    submit_button.click()
    print("Password reset request submitted.")

    # Wait for success message
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "container"))
    )
    print("✅ Reset email sent.")

    # Wait for a few seconds to allow the email to arrive
    time.sleep(10)

    # Fetch reset link from email
    reset_link = fetch_reset_link()
    print(f"Reset Link: {reset_link}")

    # Navigate to reset link
    driver.get(reset_link)

    # Wait for new password fields to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "new-password"))
    )

    # Set new password
    NEW_PASSWORD = "NewSecurePassword123!"
    new_password_input = driver.find_element(By.ID, "new-password")
    new_password_input.send_keys(NEW_PASSWORD)

    confirm_password_input = driver.find_element(By.ID, "confirm-password")
    confirm_password_input.send_keys(NEW_PASSWORD)

    # Submit new password
    reset_button = driver.find_element(By.NAME, "submit")
    reset_button.click()
    print("Password successfully reset.")

    # Verify success message
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Your password has been changed')]"))
    )
    assert "Your password has been changed" in success_message.text
    print("✅ Test Passed: Password reset successful.")



