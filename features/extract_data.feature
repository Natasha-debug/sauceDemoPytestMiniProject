Feature: Extract product data from SauceDemo inventory page

  Scenario: Extract data after successful login
    Given I am logged in with valid credentials
    When I am on the inventory page
    Then I extract all product names and descriptions from the page
    And I save them to a file
    Then I log out
    And I verify I am on the login page again
