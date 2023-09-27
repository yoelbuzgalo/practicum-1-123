import to_upper

def test_convert_to_upper_a():
    # setup
    char = 'a'
    expected = 'A'

    # invoke
    actual = to_upper.convert_to_upper(char)

    # analyze
    assert actual == expected

def test_convert_to_upper_g():
    # setup
    char = 'g'
    expected = 'G'

    # invoke
    actual = to_upper.convert_to_upper(char)

    # analyze
    assert actual == expected

def test_convert_to_upper_z():
    # setup
    char = 'z'
    expected = 'Z'

    # invoke
    actual = to_upper.convert_to_upper(char)

    # analyze
    assert actual == expected

def test_convert_to_upper_A():
    # setup
    char = 'A'
    expected = 'A'

    # invoke
    actual = to_upper.convert_to_upper(char)

    # analyze
    assert actual == expected

def test_convert_to_upper_M():
    # setup
    char = 'M'
    expected = 'M'

    # invoke
    actual = to_upper.convert_to_upper(char)

    # analyze
    assert actual == expected

def test_convert_to_upper_Z():
    # setup
    char = 'Z'
    expected = 'Z'

    # invoke
    actual = to_upper.convert_to_upper(char)

    # analyze
    assert actual == expected

def test_convert_to_upper_backtick():
    """ Edge case for 'a' """
    # setup
    char = '`'
    expected = '?'

    # invoke
    actual = to_upper.convert_to_upper(char)

    # analyze
    assert actual == expected

def test_convert_to_upper_left_brace():
    """ edge case for 'z' """
    # setup
    char = '{'
    expected = '?'

    # invoke
    actual = to_upper.convert_to_upper(char)

    # analyze
    assert actual == expected

def test_convert_to_upper_at():
    """ Edge case for 'A' """
    # setup
    char = '@'
    expected = '?'

    # invoke
    actual = to_upper.convert_to_upper(char)

    # analyze
    assert actual == expected

def test_convert_to_upper_left_bracket():
    """ edge case for 'Z' """
    # setup
    char = '['
    expected = '?'

    # invoke
    actual = to_upper.convert_to_upper(char)

    # analyze
    assert actual == expected