# Selenium Pytest Tests for Hudl Login

This repository contains automated UI tests for Hudl login functionality using **Selenium WebDriver** and **Pytest**.
The goal is to validate the login functionality under different scenarios to ensure the system behaves as expected.

## 📌 Project Overview
These tests validate the login process for the Hudl platform, checking different scenarios such as:
- Valid login credentials
- Invalid login attempts
- Resseting password
- UI behavior on incorrect inputs

# Notes 
There are other test scenarios for the Login Page that are out of scope for this test set. Please see the attached "Test Plan For Hudl Login Page" to see full, prioritised list of tests.
- Reset password - use the email password reset link
- Reset password - use the reset link in the email and input incorrect password format
- Login with newly reset password
- After password reset, login with old password
- Multiple browser sessions:
	- login in with current password on one browser session
 	- Open another browser session, login and reset password. Login with new password
  	- Check previous browser session with old user credentials.
 - Logging in with a locked account

## 🚀 Getting Started

### 1️⃣ Prerequisites
Ensure you have the following installed:
- Python (>=3.7)
- Google Chrome & ChromeDriver
- Selenium WebDriver
- Pytest

### 2️⃣ Installation
Clone this repository and install the required dependencies:

```sh
# Clone the repository
git clone https://github.com/peoguchi/Hudl-Test.git
cd Hudl-Test/Login-Tests

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Running the Tests
Run all tests using Pytest:

```sh
pytest
```
To run tests with detailed output:
```sh
pytest -v
```

Run tests in a headless browser mode:
```sh
pytest --headless
```

### 4️⃣ Test Structure
- **`tests/`**: Contains test scripts.
- **`pages/`**: Implements Page Object Model (POM) for UI elements.
- **`conftest.py`**: Sets up test configurations.
- **`pytest.ini`**: Contains Pytest configuration settings.

### 5️⃣ Reporting
To generate an HTML report:
```sh
pytest --html=report.html
```

## 🛠 Configuration
Modify `config.py` to change test parameters, such as credentials and URLs.

## 📝 Contribution Guidelines
1. Fork the repository
2. Create a feature branch
3. Implement changes and add tests
4. Submit a pull request

## 📄 License
This project is licensed under the MIT License.

---
🚀 Happy Testing! 🚀
