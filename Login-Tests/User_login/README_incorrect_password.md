# Selenium Pytest Tests for Hudl Incorrect Password Login

This repository contains automated UI tests for Hudl login functionality using **Selenium WebDriver** and **Pytest**. The tests specifically validate incorrect password login attempts implemented in `login_incorrect_password.py`.

## 📌 Project Overview
These tests validate the login process for the Hudl platform, checking different scenarios such as:
- Login attempt with an incorrect password
- Error message validation for incorrect password

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
Run the `login_incorrect_password.py` test script using Pytest:

```sh
pytest login_incorrect_password.py
```
To run tests with detailed output:
```sh
pytest -v login_incorrect_password.py
```

Run tests in a headless browser mode:
```sh
pytest --headless login_incorrect_password.py
```

### 4️⃣ Test Structure
- **`login_incorrect_password.py`**: Contains the Selenium-based incorrect password login tests.
- **`pages/`**: Implements Page Object Model (POM) for UI elements.
- **`conftest.py`**: Sets up test configurations.
- **`pytest.ini`**: Contains Pytest configuration settings.

### 5️⃣ Reporting
To generate an HTML report for `login_incorrect_password.py` tests:
```sh
pytest login_incorrect_password.py --html=report.html
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
