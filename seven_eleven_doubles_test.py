import random
import seven_eleven_doubles

def test_roll_die_12():
    # Setup
    random.seed(37) # Setting seed to 37
    sides = 12
    expected = 11

    # Invoke
    result = seven_eleven_doubles.roll_die(sides)

    # Analysis
    assert result == expected