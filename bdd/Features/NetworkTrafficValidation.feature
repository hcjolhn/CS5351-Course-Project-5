Feature: Create test cases using Selenium

  @test_Chrome
  Scenario Outline: Validate network traffic
      Given : I want to validate the network traffic
        | api                                | protocol      |
        | http://localhost:8000/forms        | POST |
        | The Lion, the Witch and the Wardrobe | C.S. Lewis  |
        | In the Garden of Beasts              | Erik Larson |
      Given : I Click on Create button
      And : I Enter a "<Name>" in Name field
      And : I Enter a "<Email>" in Email field
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
      And : Validate now
   Examples:
      |Name|Email|Message|
      |Test|test@g.com|awefawefawefbrowserchrome|