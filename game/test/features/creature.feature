Feature: Movable Creature
    A creature should be able
    to move left, right, up,
    and down.

    Scenario: Move Up
        Given The creature is at (60, 60)
        When I move it up
        Then it is now at (60, 59)

    Scenario: Move Down
        Given The creature is at (60, 60)
        When I move it down
        Then it is now at (60, 61)

    Scenario: Move Right
        Given The creature is at (60, 60)
        When I move it right
        Then it is now at (61, 60)

    Scenario: Move Left
        Given The creature is at (60, 60)
        When I move it left
        Then it is now at (59, 60)

    Scenario: Top Edge
        Given The creature is at (5, 0)
        When I move it up
        Then it is now at (5, 0)

    Scenario: Bottom Edge
        Given The creature is at (5, 599)
        When I move it down
        Then it is now at (5, 599)

    Scenario: Right Edge
        Given The creature is at (599, 0)
        When I move it right
        Then it is now at (599, 0)

    Scenario: Left Edge
        Given The creature is at (0, 0)
        When I move it left
        Then it is now at (0, 0)

