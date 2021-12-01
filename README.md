# contains some GitHub tests
1. "git clone https://github.com/yefim-mironyuk/github_task.git" to clone this package
2. "pip install -r requirements.txt" for installing necessary packages
3. Go to support/creds.py and enter your creds.
4. "pytest -v -s --tb=line --language=en test_github.py --alluredir=report_allure/" for running tests
5. "allure serve report_allure/" to open allure report
