Feature: OrangeHRM logo
  Scenario: verify login functionality with valid credentials
    Given launch chrome browser
    When open the HRM page
    And enter username "Admin" and password "admin123"
    And click on login button
    Then user must successfully login to dashboard