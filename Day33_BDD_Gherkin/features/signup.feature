Feature: Sign up Functionality
  Scenario: Successful registration
    Given the user is on the sign up page
    When the user register with valid datas
    Then the user should be redirected to login page