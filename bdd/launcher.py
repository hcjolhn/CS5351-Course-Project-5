import subprocess
from pathlib import Path
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options

subprocess.call(r'rmdir /S /Q Report_Json', shell=True)
subprocess.call(r'rmdir /S /Q Report_Html', shell=True)
subprocess.call(r'behave Features\Test.feature --tags=test_Chrome -f allure_behave.formatter:AllureFormatter -o Report_Json', shell=True)
subprocess.call(r'.\allure-2.24.1\bin\allure generate Report_Json -o Report_Html –clean', shell=True)
html = Path.cwd() / 'Report_Html//index.html'
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--disable-web-security')
driver = webdriver.Chrome(options=chrome_options)
driver.get(html.as_uri())