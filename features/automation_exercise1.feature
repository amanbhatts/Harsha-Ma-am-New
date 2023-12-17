Feature: Contact Us Form Submission

  Scenario: Fill and submit the Contact Us form
    Given the user is on the Contact Us page
    When they enter name "Aman Bhatt", email "2amanbhatts@gmail.com", subject "Is Dead", and message "Dead With python overloading"
    And they click on the submit button
    Then a success message is displayed