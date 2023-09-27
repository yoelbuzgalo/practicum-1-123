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

def test_take_turns_0():
    # Setup
    random.seed(37)
    expected = 25

    # Invoke
    result = seven_eleven_doubles.take_turn()

    # Analysis
    assert result == expected

def test_take_turns_1():
    # Setup
    random.seed(37)
    expected = 25

    # Invoke
    result = seven_eleven_doubles.take_turn()

    # Analysis
    assert result == expected

def test_take_turns_2():
    # Setup
    random.seed(37)
    expected = 12

    # Invoke
    print(seven_eleven_doubles.take_turn())
    result = seven_eleven_doubles.take_turn()

    # Analysis
    assert result == expected

def test_take_turns_3():
    # Setup
    random.seed(37)
    expected = 25

    # Invoke
    result = seven_eleven_doubles.take_turn()

    # Analysis
    assert result == expected