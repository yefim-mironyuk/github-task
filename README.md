# contains some GitHub tests
USE "pytest -v -s --tb=line --language=en .\test_github.py --alluredir=report_allure/" for running tests \n
USE "allure serve report_allure/" to open allure report
