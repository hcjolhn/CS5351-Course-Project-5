Feature: Create test cases using Selenium

  @test_Chrome
  Scenario Outline: Validate network traffic with Chrome
      Given : I Click on Create button
      And : I Enter a "<Name>" in Name field
      And : I Enter a "<Email>" in Email field
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
      And : I want to validate the network traffic
        | api                                | protocol      |
        | http://localhost:8000/forms        | POST |
   Examples:
      |Name|Email|Message|
      |Miss Little Kermit|Kermit@gmail.com|I'm a frog|


  @test_FireFox
  Scenario Outline: Validate network with Firefox
      Given : I Click on Create button
      And : I Enter a "<Name>" in Name field
      And : I Enter a "<Email>" in Email field
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
      And : I want to validate the network traffic
        | api                                | protocol      |
        | http://localhost:8000/forms        | POST |
   Examples:
      |Name|Email|Message|
      |Miss Little Kermit|Kermit@gmail.com|I'm a frog|


  @test_Edge
  Scenario Outline: Validate network traffic with Edge
      Given : I Click on Create button
      And : I Enter a "<Name>" in Name field
      And : I Enter a "<Email>" in Email field
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
      And : I want to validate the network traffic
        | api                                | protocol      |
        | http://localhost:8000/forms        | POST |
   Examples:
      |Name|Email|Message|
      |Miss Little Kermit|Kermit@gmail.com|I'm a frog|


  @test_Chrome
  Scenario Outline: Validate network request and response with Chrome
      Given : I Click on Create button
      And : I Enter a "<Name>" in Name field
      And : I Enter a "<Email>" in Email field
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
      And : I want to validate the network traffic request and response
        | api                        | protocol      | request-body | response-code |
        | http://localhost:8000/forms| POST | {"name":"Miss Little Kermit","email":"Kermit@gmail.com","message":"I'm a frog"}|201|
   Examples:
      |Name|Email|Message|
      |Miss Little Kermit|Kermit@gmail.com|I'm a frog|


  @test_FireFox
  Scenario Outline: Validate network request and response with Firefox
      Given : I Click on Create button
      And : I Enter a "<Name>" in Name field
      And : I Enter a "<Email>" in Email field
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
      And : I want to validate the network traffic request and response
        | api                        | protocol      | request-body | response-code |
        | http://localhost:8000/forms| POST | {"name":"Miss Little Kermit","email":"Kermit@gmail.com","message":"I'm a frog"}|201|
   Examples:
      |Name|Email|Message|
      |Miss Little Kermit|Kermit@gmail.com|I'm a frog|


  @test_Edge
  Scenario Outline: Validate network request and response with Edge
      Given : I Click on Create button
      And : I Enter a "<Name>" in Name field
      And : I Enter a "<Email>" in Email field
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
      And : I want to validate the network traffic request and response
        | api                        | protocol      | request-body | response-code |
        | http://localhost:8000/forms| POST | {"name":"Miss Little Kermit","email":"Kermit@gmail.com","message":"I'm a frog"}|201|
   Examples:
      |Name|Email|Message|
      |Miss Little Kermit|Kermit@gmail.com|I'm a frog|