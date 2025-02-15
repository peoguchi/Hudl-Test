from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Load environment variables from .env file
load_dotenv()

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
        # assert "login" in driver.current_url, "Login button did not navigate correctly"

        # Get email from enviromnment variables
        email = os.getenv("HUDL_EMAIL")
        
        # Find and fill in the email field
        email_input = driver.find_element(By.ID, "username")
        email_input.send_keys(email)
        # email_input.send_keys(os.getenv("HUDL_EMAIL"))
        email_input.send_keys(Keys.RETURN)
        time.sleep(2) # Wait for transition to the next step

        # Get password from enviromnment variables
        password = os.getenv("HUDL_PASSWORD")

       # Find and fill in the password field
        password_input = driver.find_element(By.ID, "password")
        # password_input.send_keys(os.getenv("HUDL_PASSWORD"))
        password_input.send_keys(password)

        # Submit login form
        password_input.send_keys(Keys.RETURN)
        time.sleep(5) # Wait for Login to complete

        # Verify login is successful
        if "dashboard" in driver.current_url:
            print("Login successful!")
        else:
            print(Login Failed!")

        except Exception as e:
            print(f"An error occured: {e}")

        # Close the browser
        finally:
        driver.quit()

# Run the test
user_login()
