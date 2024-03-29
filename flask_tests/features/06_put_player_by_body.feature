Feature: testing the first feature

Background: post and get player
    When I post a player
    And I update a players details by body

Scenario: getting player by body status code
    When I get the response status code
    Then the status code should be "202"

Scenario: getting player by body content type
    When I get the response headers
    Then response content type should be "application/json"

Scenario: getting player by body data type
    When I get the response json
    And I take position "0" from the list
    Then the response should be type "unicode"

Scenario: getting player by body response length
    When I get the response json
    Then the response should have length "8"

Scenario: getting player by body response expected fields
    When I get the response json
    Then the expected fields should be present
    | field     |
    | ACCEPTED  |
