Feature: testing the first feature

Background: post and get player
    When I post a player
    And I post another player
    And I update a match

Scenario: getting player by body status code
    When I get the response status code
    Then the status code should be "202"

Scenario: getting player by body content type
    When I get the response headers
    Then response content type should be "text/html; charset=utf-8"

Scenario: getting player by body data type
    When I get the response text
    Then the response should be type "string"

Scenario: getting player by body response length
    When I get the response text
    Then the response should have length "8"

Scenario: getting player by body response expected fields
    When I get the response text
    Then the response text should read
    | field     |
    | ACCEPTED  |

Scenario: getting player after match wins has changed
    Then the winning player should have a win

Scenario: getting player after match losses has changed
    Then the losing player should have a loss