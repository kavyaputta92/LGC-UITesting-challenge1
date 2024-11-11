# LGC-UITesting-challenge1
Python automated test using playwright

"pythonProject" contains the entire project
"test_todomvc.py" is the test file 
"allure-results" contains screenshots and video at different stages of the test execution.
"allure-report" contains the html report of the test.
"videos" folder contains sample test result video.

# TODO MVC Playwright Test with Allure Reporting

This project automates testing of the TODO MVC application using **Playwright**, **Pytest**, and **Allure** for detailed reporting.

## 🛠 Prerequisites

Ensure you have the following installed on your system:

1. **Python** (>= 3.7)
2. **Node.js** (for Playwright browser installation)
3. **Allure CLI** (for generating HTML reports)
4. **PycharmIDE** (for test execution)

### Install below Packages

```bash
##Install playwright
pip install playwright
playwright install  

## Install allure
pip install pytest allure-pytest 

### Install Allure CLI
For Windows:
Download Allure from the Allure GitHub Releases.
Extract the ZIP file to a folder (e.g., C:\allure).
Add C:\allure\bin to your system PATH.

🚀 Running the Tests
Execute the following command from your pycharm project "Scripts" folder path to run the tests and generate the Allure results:


1. Run Tests with Allure Results Directory
```bash
pytest -v --alluredir=allure-results

2. Generate the Allure HTML Report
```bash
allure serve allure-results

🛠 Troubleshooting
ModuleNotFoundError: Ensure that pytest, playwright, and allure-pytest are installed in the correct environment.
Browser Launch Error: If the browser fails to launch, make sure Playwright browsers are installed using python -m playwright install.
Allure Report Not Displayed: Check that the allure-results directory is not empty. If it is, ensure the tests are run with --alluredir=allure-results.
If you encounter this error, ensure Allure CLI is installed and added to your system PATH. Restart your terminal after making changes to the PATH.
