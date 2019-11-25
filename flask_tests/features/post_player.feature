Feature: testing the first feature

Scenario: posting player status code
    When I post a player
    And I get the response status code
    Then the status code should be "201"

Scenario: posting player content type
    When I post a player
    And I get the response headers
    Then response content type should be "application/json"

Scenario: posting player data type
    When I post a player
    And I get the response json
    Then the response should be type "dictionary"

Scenario: posting player response length
    When I post a player
    And I get the response json
    Then the response should have length "6"

Scenario: posting player response expected fields
    When I post a player
    And I get the response json
    Then the expected fields should be present
    | field     |
    | firstname |
    | lastname  |
    | losses    |
    | playerid  |
    | ratio     |
    | wins      |

Scenario: posting player response expected data types
    When I post a player
    And I get the response json
    Then the expected fields should be present
    | field     | data_type |
    | firstname | unicode   |
    | lastname  | unicode   |
    | losses    | int       |
    | playerid  | unicode   |
    | ratio     | float     |
    | wins      | int       |

