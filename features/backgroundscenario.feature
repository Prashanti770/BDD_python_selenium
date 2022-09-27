#
##  Background : Executing certain steps before each scenario - it is a feature
#Feature: Orange HRM Login
#  Background: common steps
#    Given I launch browser
#    When I Open OrangeHrm page
#    And enter username as "Admin" and password as "admin123"
#    And click on Login button
#
#  Scenario:  Login to OrangeHRM with valid Parameters
#    Then User must be successfully logged in to the dashboard page
#
#  Scenario: Logout
#    Then User must be able to Logout
