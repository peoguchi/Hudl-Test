# Selenium Pytest Tests for Hudl Password Reset

This repository contains automated UI tests for Hudl password reset functionality using **Selenium WebDriver** and **Pytest**. The tests specifically validate the password reset process implemented in `password_reset.py`.

## 📌 Project Overview
These tests validate the password reset functionality for the Hudl platform, checking different scenarios such as:
- Requesting a password reset with a registered email
- Handling password reset requests with unregistered emails
- Validating error messages and success messages
- UI behavior upon password reset request submission

Note: This test does not include validating the password reset link sent by email.

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
Run the `password_reset.py` test script using Pytest:

```sh
pytest password_reset.py
```
To run tests with detailed output:
```sh
pytest -v password_reset.py
```

Run tests in a headless browser mode:
```sh
pytest --headless password_reset.py
```

### 4️⃣ Test Structure
- **`password_reset.py`**: Contains the Selenium-based password reset tests.
- **`pages/`**: Implements Page Object Model (POM) for UI elements.
- **`conftest.py`**: Sets up test configurations.
- **`pytest.ini`**: Contains Pytest configuration settings.

### 5️⃣ Reporting
To generate an HTML report for `password_reset.py` tests:
```sh
pytest password_reset.py --html=report.html
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

