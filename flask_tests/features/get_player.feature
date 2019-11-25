Feature: testing the first feature

Scenario: getting player by id status code
    When I get a player by id
    And I get the response status code
    Then the status code should be "201"

Scenario: getting player by id content type
    When I get a player by id
    And I get the response headers
    Then response content type should be "application/json"

Scenario: getting player by id data type
    When I get a player by id
    And I get the response json
    Then the response should be type "dictionary"

Scenario: getting player by id response length
    When I get a player by id
    And I get the response json
    Then the response should have length "6"

Scenario: getting player by id response expected fields
    When I get a player by id
    And I get the response json
    Then the expected fields should be present
    | field     |
    | firstname |
    | lastname  |
    | losses    |
    | playerid  |
    | ratio     |
    | wins      |

Scenario: getting player by id response expected data types
    When I get a player by id
    And I get the response json
    Then the expected fields should be present
    | field     | data_type |
    | firstname | unicode   |
    | lastname  | unicode   |
    | losses    | int       |
    | playerid  | unicode   |
    | ratio     | float     |
    | wins      | int       |

#######################################

Scenario: getting player by body status code
    When I get a player by id
    And I get the response status code
    Then the status code should be "201"

Scenario: getting player by body content type
    When I get a player by id
    And I get the response headers
    Then response content type should be "application/json"

Scenario: getting player by body data type
    When I get a player by id
    And I get the response json
    Then the response should be type "dictionary"

Scenario: getting player by body response length
    When I get a player by id
    And I get the response json
    Then the response should have length "6"

Scenario: getting player by body response expected fields
    When I get a player by id
    And I get the response json
    Then the expected fields should be present
    | field     |
    | firstname |
    | lastname  |
    | losses    |
    | playerid  |
    | ratio     |
    | wins      |

Scenario: getting player by body response expected data types
    When I get a player by id
    And I get the response json
    Then the expected fields should be present
    | field     | data_type |
    | firstname | unicode   |
    | lastname  | unicode   |
    | losses    | int       |
    | playerid  | unicode   |
    | ratio     | float     |
    | wins      | int       |