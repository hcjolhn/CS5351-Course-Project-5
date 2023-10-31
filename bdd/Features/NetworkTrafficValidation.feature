Feature: Create test cases using Selenium

  @test_Chrome
  Scenario Outline: Validate network traffic
#      Given : I want to validate the network traffic
      Given : I Click on Create button
      And : I Enter a "<Name>" in Name field
      And : I Enter a "<Email>" in Email field
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
   Examples:
      |Name|Email|Message|
      |Test|test@g.com|awefawefawefbrowserchrome|