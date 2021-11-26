# contains some GitHub tests
USE "pip install -r requirements.txt" for installing necessary packages

USE "pytest -v -s --tb=line --language=en .\test_github.py --alluredir=report_allure/" for running tests

USE "allure serve report_allure/" to open allure report
