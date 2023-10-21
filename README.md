# CS5351-Course-Project-5
## Gudie to start web app for test
1. install Node.js (https://nodejs.org/en)
2. Go to project directory
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
3. Go to api directory
4. mvn spring-boot:run
5. import api_postman.json in Postman and test the api.

## Guide to start automation tools
### Prerequisites
- Python
### Steps
1. pip install -r requirement.txt
2. Run commands:
  To run all the present feature files: behave Feature -f allure_behave.formatter:AllureFormatter -o Report_Json

  To run a single feature file: behave Features/Test.feature -f allure_behave.formatter:AllureFormatter -o Report_Json

  To run the single scenario using the tag name given to the scenario: behave Features/Test.feature --tags=test -f allure_behave.formatter:AllureFormatter -o Report_Json

  To run the the test scenario using the given tag name from all the present feature files: behave Features --tags=test -f allure_behave.formatter:AllureFormatter -o Report_Json
3. Generate HTML Report:
