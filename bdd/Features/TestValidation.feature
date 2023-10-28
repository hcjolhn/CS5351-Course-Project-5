Feature: Create test cases using Selenium

  @test
  Scenario Outline: Create a record
    Given  : I Click on Create button
    And   : I Enter a "<Name>" in Name field and validate
  Examples:
    |Name|Email|Message|
    |123|test@g.com|awefawefawef|