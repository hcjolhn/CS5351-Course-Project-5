# CS5351-Course-Project-5
## Gudie to start web app for test
1. install Node.js (https://nodejs.org/en)
2. Go to "web-app-for-test" directory
3. npm i
4. npm start

## Guide to start api
### Prerequisites
- JDK
- Maven
- Docker
### Steps
1. Install Docker and run a container for MySQL
docker run -d -e MYSQL_ROOT_PASSWORD=<password> -e MYSQL_DATABASE=db --name mysqldb -p 3307:3306 mysql:8.0
2. run form.sql to create table
3. Go to "api" directory
4. mvn spring-boot:run
5. import api_postman.json in Postman and test the api.

## Guide to start automation tools
### Prerequisites
- Python
### Steps
1. Go to "bdd" directory
2. execute "start.bat" in "bdd" directory
   
### Remarks (Before execute start.bat)
   1. You may edit test.csv in "Features" directory to specific test examples for testing. After automated test starts, the examples in csv will be transformed into specific feature file.
   2. You may edit line 10 of launcher.py in "bdd" directory to run differet test cases. The default test case will be Add, Edit, Delete record with different browsers.
   #### Below are the samples of line 10 in launcher.py
   To run all test cases: behave Feature -f allure_behave.formatter:AllureFormatter -o Report_Json

   To run Add, Edit, Delete record test case: behave Features/TestCSV.feature -f allure_behave.formatter:AllureFormatter -o Report_Json

   To run Network Traffic Validation test case: behave Features/NetworkTrafficValidation.feature -f allure_behave.formatter:AllureFormatter -o Report_Json

   To run Output Validation test case: behave Features/TestOutputValidation.feature -f allure_behave.formatter:AllureFormatter -o Report_Json

   To run Validation test case: behave Features/TestValidation.feature -f allure_behave.formatter:AllureFormatter -o Report_Json

   To run Submission Validation test case: behave Features/TestValidateSubmit.feature -f allure_behave.formatter:AllureFormatter -o Report_Json

   #### Below are some commands for running specific testing scenario 

   To run the single scenario using the tag name given to the scenario: behave Features/Test.feature --tags=test -f allure_behave.formatter:AllureFormatter -o Report_Json

   To run the the test scenario using the given tag name from all the present feature files: behave Features --tags=test -f allure_behave.formatter:AllureFormatter -o Report_Json
