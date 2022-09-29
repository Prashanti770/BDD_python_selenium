Feature: OrangeHRM login
  Scenario:  Login to OrangeHRM with valid Parameters
    Given launch browser
    When I Open OrangeHrm page
    And enter username as "Admin" and password as "admin123"
    And click on Login button
    Then User must be successfully logged in to the dashboard page

