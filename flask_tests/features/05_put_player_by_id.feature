Feature: testing the first feature

Background: post and get player
    When I post a player
    And I update a players details by id

Scenario: getting player by id status code
    When I get the response status code
    Then the status code should be "200"

Scenario: getting player by id content type
    When I get the response headers
    Then response content type should be "application/json"

Scenario: getting player by id data type
    When I get the response json
    And I take position "0" from the list
    Then the response should be type "dictionary"

Scenario: getting player by id response length
    When I get the response json
    And I take position "0" from the list
    Then the response should have length "6"

Scenario: getting player by id response expected fields
    When I get the response json
    And I take position "0" from the list
    Then the expected fields should be present
    | field     |
    | firstname |
    | lastname  |
    | losses    |
    | playerid  |
    | ratio     |
    | wins      |

Scenario: getting player by id response expected data types
    When I get the response json
    And I take position "0" from the list
    Then the expected fields should be present
    | field     | data_type |
    | firstname | unicode   |
    | lastname  | unicode   |
    | losses    | int       |
    | playerid  | unicode   |
    | ratio     | float     |
    | wins      | int       |
