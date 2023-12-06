Feature: Create output cases using Selenium

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
		|"Fergusssss"|"test@example.com22"|"test message"|
