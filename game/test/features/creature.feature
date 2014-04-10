Feature: Movable Creature
    A creature should be able
    to move left, right, up,
    and down.

    Scenario: Move Up
        Given The creature is at (60, 60)
        When I move it up
        Then It is now at (60, 59)

    Scenario: Move Down
        Given The creature is at (60, 60)
        When I move it down
        Then It is now at (60, 61)

    Scenario: Move Right
        Given The creature is at (60, 60)
        when I move it right
        Then it is now at (61, 60)

    Scenario: Move Left
        Given The creature is at (60, 60)
        when I move it left
        Then it is now at (59, 60)
