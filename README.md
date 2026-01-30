# n11 Login Automation (Python + Selenium, POM)

This repository contains a basic Selenium automation project for n11 login scenarios, implemented in **Python** using **Page Object Model (POM)** and **pytest**.

## Tech Stack
- Python
- Selenium WebDriver
- pytest
- webdriver-manager

## Project Structure
n11-login-automation/
├─ pages/
├─ tests/
├─ utils/
├─ requirements.txt
└─ README.md

## Setup
1. Create and activate virtual environment:
   - `python -m venv .venv`
   - Windows: `.venv\Scripts\activate`

2. Install dependencies:
   - `pip install -r requirements.txt`

## Run Tests
Run all tests:
- `python -m pytest -q`

## Test Scope
Automated scenarios (basic level):
- Email/Phone input accepts valid formats
- Login fails with incorrect password (error message displayed)
- Login is blocked when required fields are empty (validation displayed)

Manual-only note:
- Valid login scenario is executed manually due to credential/security constraints.
