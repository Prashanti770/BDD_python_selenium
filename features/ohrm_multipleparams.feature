#  Executing scenario with multiple sets of data
#  Data will be in single or multiple steps
#  Scenario - executes only single time
#  Scenario outline - executes multiple times, here use "Examples" Gherkin keyword
#  Examples have header part and multiple sets of data, header part text will be kept in double quotes with Angular barckets in step
#  To seperate data in we use | pipe symbol with tab space
#  To align the code -> ctrl+A (select code)-> In options , code ->Reformat code : ctrl+alt+l
#  Scenario Outline is always followed by Examples
Feature: OrangeHRM login

  Scenario:  Login to OrangeHRM with valid Parameters
    Given I launch browser
    When I Open OrangeHrm page
    And enter username as "Admin" and password as "admin123"
    And click on Login button
    Then User must be successfully logged in to the dashboard page

  Scenario Outline:  Login to OrangeHRM with multiple Parameters
    Given I launch browser
    When I Open OrangeHrm page
    And enter username as "<username>" and password as "<password>"
    And click on Login button
    Then User must be successfully logged in to the dashboard page

    Examples:
      | username | password |
      | Admin    | admin123 |
      | admin    | admin    |
      | asd      | aass     |


