Feature: Create test cases using Selenium

  @test_Chrome
  Scenario Outline: Create a record with Chrome
      Given : I Click on Create button
      And : I Enter a error "<Name>" in Name field
      And : I Enter a error "<Email>" in Email field
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
   Examples:
      |Name|Email|Message|
      |123|testg.com|awefawefawefbrowserchrome|