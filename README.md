# CS5351-Course-Project-5
## Gudie to start web app for test
1. install Node.js (https://nodejs.org/en)
2. Go to project directory
3. npm i
4. npm start

## Guid to start api
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
