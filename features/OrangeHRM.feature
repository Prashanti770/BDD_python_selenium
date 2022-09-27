Feature: OrangeHRM Login

  Scenario: Logo Present on Orange HRM page
    Given Launch Chrome Browser
    When open HRM page
    Then verfiy that logo present o page
    And close Browser

#    Implement the above steps - to write code
#   " behave features\OrangeHRM.feature "  -- executing command
#  for all feature/scenarios executing : " behave ./feature "
#  Gives un implemented steps definition in python format
#  for each sentence created there is step definition for it
#
# "  behave -f allure_behave.formatter:AllureFormatter -o reports/ features/ohrm_multipleparams.feature " - for allure reports