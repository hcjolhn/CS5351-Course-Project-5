Feature: Create test cases using Selenium

@browser:Chrome
Scenario Outline: Create a record with Chrome
    Given: I Click on Create button
    And: I Enter a "<Name>" in Name field
    And: I Enter a "<Email>" in Email field
    And: I Enter a "<Message>" in Message field
    And: I Click on Submit button
 Examples:
    |Name|Email|Message|
    |Test|test@g.com|awefawefawefbrowser:chrome|
    
@browser:Firefox
Scenario Outline: Create a record with Firefox
    Given: I Click on Create button
    And: I Enter a "<Name>" in Name field
    And: I Enter a "<Email>" in Email field
    And: I Enter a "<Message>" in Message field
    And: I Click on Submit button
 Examples:
    |Name|Email|Message|
    |Test|test@g.com|awefawefawefbrowser:firefox|
    
@browser:Edge
Scenario Outline: Create a record with Edge
    Given: I Click on Create button
    And: I Enter a "<Name>" in Name field
    And: I Enter a "<Email>" in Email field
    And: I Enter a "<Message>" in Message field
    And: I Click on Submit button
 Examples:
    |Name|Email|Message|
    |Test|test@g.com|awefawefawefbrowser:edge|
    
@browser:IE
Scenario Outline: Create a record with IE
    Given: I Click on Create button
    And: I Enter a "<Name>" in Name field
    And: I Enter a "<Email>" in Email field
    And: I Enter a "<Message>" in Message field
    And: I Click on Submit button
 Examples:
    |Name|Email|Message|
    |Test|test@g.com|awefawefawefbrowser:IE|
