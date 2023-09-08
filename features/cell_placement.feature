Feature: The user put cells in the board while the game is in cell placement mode

  Scenario: The player puts the first live cell in an empty board
    Given the game is in cell placement mode
    And the dimensions of the board are 8x8
    And the state of the board is
      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
    When the player puts a live cell in position (2, 7)
    Then there should be a live cell in position (2, 7)
    And the state of the board should be
      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   | o |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |


  Scenario: The player puts a second live cell in the board
    Given the game is in cell placement mode
    And the dimensions of the board are 8x8
    And the state of the board is
      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
      |   |   |   |   |   |   |   |   |
      |   |   | o |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
    When the player puts a live cell in position (3, 4)
    Then there should be a live cell in position (3, 4)
    And the state of the board should be
      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
      |   |   |   |   |   |   |   |   |
      |   |   | o |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   | o |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |


  Scenario: The player puts a third live cell in the board
    Given the game is in cell placement mode
    And the dimensions of the board are 8x8
    And the state of the board is
      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
      |   |   |   |   |   |   |   |   |
      |   |   | o |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   | o |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
    When the player puts a live cell in position (4, 6)
    Then there should be a live cell in position (4, 6)
    And the state of the board should be
      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
      |   |   |   |   |   |   |   |   |
      |   |   | o |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   | o |   |
      |   | o |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |


  Scenario: The player puts a live cell while the game is not in cell placement mode
    Given the game is started
    And the dimensions of the board are 8x8
    And the game is in simulation mode
    When the player puts a live cell in position (3, 4)
    Then an error is returned to the user



