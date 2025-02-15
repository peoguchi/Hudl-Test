# Hudl Test
 Repository for test automation
This file contains details of the test script that will be run.


# Approach to Testing the Hudl.com Login Page
The test script follows a structured automation testing approach using Selenium WebDriver and Pytest. The goal is to validate the login functionality under different scenarios to ensure the system behaves as expected.


# Testing Strategy
The script implements a data-driven testing approach where different sets of credentials (valid and invalid) are used to verify login behavior. It uses UI-based functional testing to interact with the login page.


# Test Script Structure
Setup and Teardown using Pytest Fixtures
- A driver() fixture is used to initialize the Chrome WebDriver before each test and close it after execution.
- This ensures proper resource management.


# Test scenarios
Valid Login: Ensures the user can log in with correct credentials.
Invalid Login: Ensures an error message appears for incorrect credentials.
Reset password: Ensures user is able to successfully reset their password and login with their new credentials.
Reset password failure: Ensures if user enters incorrect credentials, password reset fails correctly.
Reset password failure: Ensures user cannot set new password with incorrect password failure.  
Reset password failure: Ensures user successfully resets their passwordd and is unable to login with old credentials.


# Key Considerations
- Why Selenium?
	Selenium allows direct interaction with the web elements.
	It provides cross-browser support.
	Supports automation of real user flows.
- Why Pytest?
	Pytest provides a simple test structure.
	Supports fixtures for setup and teardown.
	Allows for parameterized testing (if needed in the future).
- Handling Dynamic Elements
	time.sleep() is used for simplicity, but explicit waits (WebDriverWait) can be used for dynamic elemen 


# Feature Enhancements
- Implement explicit waits instead of time.sleep().
- Use data-driven testing (via CSV, Excel, or Pytest parameters) for multiple test cases.
- Extend tests to validate:
	Login with a locked account.
	Browser compatibility.
- Logout test to ensure user is properly logged out and cannot access the dashboard after logging out
- Logging in to multiple devices to verify how the user's current session is affected and handled.
- SQL injections to ensure input fields are protected against malicious input.


# Reporting and logging
- Generate Detailed Test Reports using Pytest HTML Reports.
Integrate with Allure Reports for detailed logs and screenshots.


# Risks
- Functional Risks	
	UI element changes: If Hudl updates the login page (e.g., changing the ID or XPath of input fields or buttons), the test may fail due to element not found errors.
- Mitigation: 
Use robust locators (like By.NAME or By.CSS_SELECTOR) and implement explicit waits to handle dynamic elements.

- Rate Limiting or Account Locking:
	Multiple invalid login attempts may lock the account, preventing further tests.
- Mitigation: Use a dummy test account and avoid excessive invalid login attempts in a short period.

- Performance Risks
	Slow page load or network issues causing the login page to load slowly, leading to timeout errors.
- Mitigation: Use explicit waits (WebDriverWait) instead of time.sleep() to handle dynamic elements.

Security Risks:
- Exposing private data in the code by storing plain text credentials in the script.
- Mitigation: use environment variables or secure vaults, AWS, which hashs out sensitive data.

Test Maintainability Risks:
- Hardcoded data makes the test difficult to maintain.
- Mitigation: Use configuration files oor parameterised to manage test data


Addressing these risks and integrating these considerations ensures that the Hudl.com login automation test remains robust, reliable, scalable and maintainable.

