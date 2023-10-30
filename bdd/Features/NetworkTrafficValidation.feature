Feature: Create test cases using Selenium

  @validate_network_request_call
  Scenario Outline: Validate network request call
      Given : Validate network request call
      And : Check "<API>" is called
      And : Check "<HttpProtocol>" is used
   Examples:
      |API|HttpProtocol|
      |http://localhost:8000/forms|POST|
