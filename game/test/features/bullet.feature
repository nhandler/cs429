Feature: Movable Bullet
    A bullet should be able
    to move left, right, up,
    and down.

    Scenario: Move Up
        Given The bullet is at (60, 60) moving up
        When The bullet moves
        Then The bullet is now at (60, 59)

    Scenario: Move Down
        Given The bullet is at (60, 60) moving down
        When The bullet moves
        Then The bullet is now at (60, 61)

    Scenario: Move Right
        Given The bullet is at (60, 60) moving right
        When The bullet moves
        Then The bullet is now at (61, 60)

    Scenario: Move Left
        Given The bullet is at (60, 60) moving left
        When The bullet moves
        Then The bullet is now at (59, 60)
