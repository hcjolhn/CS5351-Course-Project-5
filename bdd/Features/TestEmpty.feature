Feature: Create output cases using Selenium

	@test_Chrome
	Scenario Outline: Create a record with Chrome
		Given : I Click on Create button
		And : I Enter a "<Name>" in Name field
		And : I Enter a "<Email>" in Email field
		And : I Enter a "<Message>" in Message field
		And : I Click on Submit button
	Examples:
		|Name|Email|Message|
		|"Fergusssss"|"test@example.com22"|"test message"|
