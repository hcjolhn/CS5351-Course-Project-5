Feature: Create test cases using Selenium

  @test_Chrome
  Scenario Outline: Chrome Test
      Given : I Click on Create button
      And : I Enter a "<Name>" in Name field
      And : I Enter a "<Email>" in Email field
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
      And : I Click on Back button
      And : I Click on Edit button with the "1"-th row
      And : I Clear Name field
      And : I Clear Email field
      And : I Clear Message field
      And : I Enter a "<Name2>" in Name field
      And : I Enter a "<Email2>" in Email field
      And : I Enter a "<Message2>" in Message field
      And : I Click on Submit button
      And : I Click on Back button
      And : Check the "1"-th row "<Name2>", "<Email2>", "<Message2>"
      And : I Click on Delete button with the "1"-th row
   Examples:
      |Name|Email|Message|Name2|Email2|Message2|
      |Chrome|chrome@example.com|I'm a Chrome|Chrome2|chrome2@example.com|I'm a Chrome2|

  @test_FireFox
  Scenario Outline: Firefox Test
      Given : I Click on Create button
      And : I Enter a "<Name>" in Name field
      And : I Enter a "<Email>" in Email field
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
      And : I Click on Back button
      And : I Click on Edit button with the "1"-th row
      And : I Clear Name field
      And : I Clear Email field
      And : I Clear Message field
      And : I Enter a "<Name2>" in Name field
      And : I Enter a "<Email2>" in Email field
      And : I Enter a "<Message2>" in Message field
      And : I Click on Submit button
      And : I Click on Back button
      And : Check the "1"-th row "<Name2>", "<Email2>", "<Message2>"
      And : I Click on Delete button with the "1"-th row
   Examples:
      |Name|Email|Message|Name2|Email2|Message2|
      |Firefox|firefox@example.com|I'm a Firefox|Firefox2|firefox2@example.com|I'm a Firefox2|

  @test_Edge
  Scenario Outline: Edge Test
      Given : I Click on Create button
      And : I Enter a "<Name>" in Name field
      And : I Enter a "<Email>" in Email field
      And : I Enter a "<Message>" in Message field
      And : I Click on Submit button
      And : I Click on Back button
      And : I Click on Edit button with the "1"-th row
      And : I Clear Name field
      And : I Clear Email field
      And : I Clear Message field
      And : I Enter a "<Name2>" in Name field
      And : I Enter a "<Email2>" in Email field
      And : I Enter a "<Message2>" in Message field
      And : I Click on Submit button
      And : I Click on Back button
      And : Check the "1"-th row "<Name2>", "<Email2>", "<Message2>"
      And : I Click on Delete button with the "1"-th row
   Examples:
      |Name|Email|Message|Name2|Email2|Message2|
      |Edge|edge@example.com|I'm a Edge|Edge2|edge2@example.com|I'm a Edge2|