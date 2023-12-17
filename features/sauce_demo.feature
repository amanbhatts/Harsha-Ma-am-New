Feature: Login to the SauceDemo website

  Scenario: User logs in with valid credentials
    Given the user is on the Sauce Demo login page
    When they enter username "standard_user" and password "secret_sauce"
    And they click on the login button
    Then they should be logged in successfully