# LGC-UITesting-challenge1
Python test project using playwright

# TODO MVC Playwright Test with Allure Reporting

This python project automates testing of the TODO MVC application using **Playwright**, **Pytest**, and **Allure** for detailed reporting.

1. **pythonProject** folder contains the entire project
2. **test_todomvc.py** is the test file 
3. **allure-results** folder contains screenshots and video at different stages of the test execution.
4. **allure-report** folder contains the html report of the test.
5. **videos** folder contains sample test result video.

## 🛠 Prerequisites

Ensure you have the following installed on your system:

1. **Python** (>= 3.7)
2. **Node.js** (for Playwright browser installation)
3. **Allure CLI** (for generating HTML reports)
4. **PycharmIDE** (for test execution)
   
## Setup

```bash
git clone https://github.com/kavyaputta92/LGC-UITesting-challenge1.git
cd LGC-UITesting-challenge1
```
## Install below Packages
Install Playwright using the following commands:

```bash
##Install playwright
pip install playwright
playwright install  

## Install allure
pip install pytest allure-pytest 
```
## Install Allure CLI
For Windows:
- Download Allure from the Allure GitHub Releases.
- Extract the ZIP file to a folder (e.g., C:\allure).
- Add C:\allure\bin to your system PATH.

## 🚀 Running the Tests
Execute the following command from your pycharm project "Scripts" folder path to run the tests and generate the Allure results:

1. Run Tests with Allure Results Directory
```bash
pytest -v --alluredir=allure-results
```
2. Generate the Allure HTML Report
```bash
allure serve allure-results
```
# After execution test results are present under allure-results folder, html report present under allure-report folder.
## 🛠 Troubleshooting
- **ModuleNotFoundError:** Ensure that pytest, playwright, and allure-pytest are installed in the correct environment.
- **Browser Launch Error:** If the browser fails to launch, make sure Playwright browsers are installed using python -m playwright install.
- **Allure Report Not Displayed:** Check that the allure-results directory is not empty. If it is, ensure the tests are run with --alluredir=allure-results.
If you encounter this error, ensure Allure CLI is installed and added to your system PATH. Restart your terminal after making changes to the PATH.
