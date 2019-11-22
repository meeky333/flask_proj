Feature: testing the first feature

  Scenario: posting player status code
      When I post a player
      And I get the response status code
      Then the status code should be "200"
      
  Scenario: posting player content type
      When I post a player
      And I get the response headers
      Then response content type should be "application/json; charset=UTF-8"

  Scenario: posting player data type
      When I post a player
      And I get the response json
      Then the response should be type "dictionary"

  Scenario: posting player response length
      When I post a player
      And I get the response json
      Then the response should have length "6"