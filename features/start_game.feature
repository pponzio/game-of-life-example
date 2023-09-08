Feature: Create a new game

  Scenario: Start a new game
    Given the game is not started
    When we create a new game with an 8x8 board
    Then the game should be in cells placement mode
    And the state of the board should be
      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |