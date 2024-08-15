#Feature: showing off behave
#
#  Scenario: run a simple test
#     Given Open google
#      When we implement a test
#      Then behave will test it for us!
#
#  Scenario

Feature: Open Google

  Scenario: Open Google homepage
    Given the browser is open
    When I navigate to Google
    Then the Google homepage should be displayed

#    Given the browser is open
    When I search for search query
    Then I should see search results for search query