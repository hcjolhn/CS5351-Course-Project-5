Feature: Create test cases using Selenium

  @test_Chrome
  Scenario Outline: Create a record with Chrome
      Given : I Click on Create button
      And : I Enter a "<Name>" in Name field and validate
      And : I Enter a "<Email>" in Email field and validate
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
   Examples:
      |Name|Email|Message|
      |123|testg.com|awefawefawefbrowserchrome|


