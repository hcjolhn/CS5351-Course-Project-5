# SeleniumPython
In this selenium python project BDD Framework created alsong with selenium python to automate web test cases and api testing. I have also added the allure reports to display the full and detailed presentation of the test result. 



Installation:

To install Selenium : pip install selenium (Used to run the test)

To install Webdriver Manager: pip install webdriver-manager (Chrome or other browser drivers)

To install Behave: pip install behave (The BDD Framework plugin)

To install allure: pip install allure-behave (to generate the reports) Also need to install one more package pip install allure-python-commons

Or

pip install -r requirement.txt

The Run commands:

To run all the present feature files: behave Feature -f allure_behave.formatter:AllureFormatter -o Report_Json

To run a single feature file: behave Features/Test.feature -f allure_behave.formatter:AllureFormatter -o Report_Json

To run the single scenario using the tag name given to the scenario: behave Features/Test.feature --tags=test -f allure_behave.formatter:AllureFormatter -o Report_Json

To run the the test scenario using the given tag name from all the present feature files: behave Features --tags=test -f allure_behave.formatter:AllureFormatter -o Report_Json



To Generate the HTML Report:
1. Go to allure-2.24.1\bin directory
2. Run command: allure generate ../../Report_Json -o ../../Report_Html --clean

