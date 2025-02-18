# Password Reset Test - Hudl

## Overview
This repository contains an automated test script (`reset.py`) designed to verify the password reset functionality on Hudl. The test is implemented using Selenium WebDriver and pytest for automation and validation.

## Note
This test is currently failing because of it's somewhat complex nature in calling a different website service to validate an email received from an external client that generates temporary email addresses.
## Prerequisites
Before running the test, ensure the following dependencies are installed:

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (Ensure the version matches your Chrome installation)
- [Selenium](https://selenium-python.readthedocs.io/installation.html): Install via pip
- [pytest](https://docs.pytest.org/en/stable/getting-started.html): Install via pip
- [python-dotenv](https://pypi.org/project/python-dotenv/): Install via pip

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/peoguchi/Hudl-Test.git
   cd Hudl-Test/Login-Tests/Password_reset
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set Up Environment Variables:**
   Create a `.env` file in the `Password_reset` directory with the following content:
   ```env
   HUDL_EMAIL=your_email@example.com
   HUDL_PASSWORD=your_password
   ```
   Replace `your_email@example.com` and `your_password` with actual test credentials.

## Test Execution

To run the test, execute the following command:
```bash
pytest reset.py
```

The script performs the following steps:
1. Navigates to the Hudl password reset page.
2. Enters the provided email address.
3. Submits the password reset request.
4. Waits for the reset email to be received.
5. Attempts to reset the password using the reset link.

## Known Issues & Failures

The `reset.py` test script may fail due to the following reasons:

1. **Temporary Email Service Limitations:**
    - The script relies on `tempmailo.com` to receive the password reset email. If the email structure changes, the test may fail.
    - Hudl may have security measures in place that block emails sent to temporary email providers.


## Suggested Improvements
- **Use a Persistent Email Account:** Instead of relying on a temporary email service, consider using a real email account for consistent results.
- **Logging and Reporting:** Implement logging for better debugging and reporting mechanisms to track test runs and failures.

## License
This project is licensed under the MIT License. See [LICENSE](../LICENSE) for more details.

---

This README file provides all necessary details to understand, install, and troubleshoot the password reset test script.

