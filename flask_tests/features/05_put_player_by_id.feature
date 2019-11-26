Feature: testing the first feature

Background: post and get player
    When I post a player
    And I update a players details by id

Scenario: getting player by id status code
    When I get the response status code
    Then the status code should be "202"

Scenario: getting player by id content type
    When I get the response headers
    Then response content type should be "application/json"

Scenario: getting player by id data type
    When I get the response json
    And I take position "0" from the list
    Then the response should be type "unicode"

Scenario: getting player by id response length
    When I get the response json
    Then the response should have length "8"

Scenario: getting player by id response expected fields
    When I get the response json
    Then the expected fields should be present
    | field     |
    | ACCEPTED  |
