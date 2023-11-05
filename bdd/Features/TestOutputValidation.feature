Feature: Create output cases using Selenium

  @test_Chrome
  Scenario Outline: Create a record with Chrome
      Given : I Click on Create button
      And : I Enter a "<Name>" in Name field
      And : I Enter a "<Email>" in Email field
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
      And : I Click on Back button
      And : Check the new input "<Name>", "<Email>", "<Message>"
   Examples:
      |Name|Email|Message|
      |1|1@g.com|1|

  @test_Chrome
  Scenario Outline: Create a record with Chrome
      Given : I Click on Create button
      And : I Enter a "<Name>" in Name field
      And : I Enter a "<Email>" in Email field
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
      And : I Click on Back button
      And : Check the new input "<Name>", "<Email>", "<Message>"
   Examples:
      |Name|Email|Message|
      |2|2@g.com|2|

  @test_Chrome
  Scenario Outline: Create a record with Chrome
      Given : I Click on Create button
      And : I Enter a "<Name>" in Name field
      And : I Enter a "<Email>" in Email field
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
      And : I Click on Back button
      And : Check the new input "<Name>", "<Email>", "<Message>"
   Examples:
      |Name|Email|Message|
      |3|3@g.com|3|

  @test_Chrome
  Scenario Outline: Edit a record with Chrome
      Given : I Click on Delete button with the "1"-th row 
   Examples:
      |Name|Email|Message|
      |none|none@g.com|none|

  @test_Chrome
  Scenario Outline: Edit a record with Chrome
      Given : I Click on Edit button with the "1"-th row 
      And : I Clear Name field
      And : I Clear Email field
      And : I Clear Message field
      And : I Enter a "<Name>" in Name field
      And : I Enter a "<Email>" in Email field
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
      And : I Click on Back button
      And : Check the "1"-th row "<Name>", "<Email>", "<Message>"
   Examples:
      |Name|Email|Message|
      |new_1|new_1@g.com|new_1|
