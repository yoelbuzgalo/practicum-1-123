import dogs_age

def test_human_years_0():
    # Setup
    dog_age = 0
    expected = 0

    # Invoke
    result = dogs_age.human_years(dog_age)

    # Analysis
    assert result == expected

def test_human_years_1():
    # Setup
    dog_age = 1
    expected = 15

    # Invoke
    result = dogs_age.human_years(dog_age)

    #nalysis
    assert result == expected

def test_human_years_2():
    # Setup
    dog_age = 2
    expected = 24

    # Invoke
    result = dogs_age.human_years(dog_age)

    #nalysis
    assert result == expected

def test_human_years_7():
    # Setup
    dog_age = 7
    expected = 49

    # Invoke
    result = dogs_age.human_years(dog_age)

    #nalysis
    assert result == expected