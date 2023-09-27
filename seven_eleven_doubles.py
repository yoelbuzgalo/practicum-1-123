import random

def roll_die(sides):
    """
    This function returns a random number between 1 to the total amount of sides of a die
    """
    random_num = random.randint(1, sides) # Generates a random integer number between 1 to the total amount of sides
    return random_num # Returns the random_num

def take_turn():
    """ 
    This function calls roll_die function twice, and returns a value of how much points the player gets for the results of the dies (game)
    """
    sides = 6 # Set sides to 6
    die_1 = roll_die(sides) # Calls roll_die function to get a random number result of die 1
    die_2 = roll_die(sides) # Calls roll_die function to get a random number result of die 2

    if (die_1 + die_2) == 7:
        # If both dies sums up to 7, player gets 21 points
        return 21
    elif (die_1 + die_2) == 11:
        # If both dies sums up to 11, player gets 25 points
        return 25
    elif die_1 == die_2:
        # If both dies are same numbers, player gets the sum of both dies
        return (die_1 + die_2)
    else:
        # Otherwise player gets 0 points
        return 0

def main():
    """
    Main entry of this program
    """
    random.seed(37) # Setting seed to 37 to see output
    print(random.randint(1,6)) # Checking the result of first random number generation of random num between 1-12
    print(random.randint(1,6)) # Checking the result of first random number generation of random num between 1-12
    print(random.randint(1,6)) # Checking the result of first random number generation of random num between 1-12
    print(random.randint(1,6)) # Checking the result of first random number generation of random num between 1-12
    print(random.randint(1,6)) # Checking the result of first random number generation of random num between 1-12
    print(random.randint(1,6)) # Checking the result of first random number generation of random num between 1-12
    print(random.randint(1,6)) # Checking the result of first random number generation of random num between 1-12
    print(random.randint(1,6)) # Checking the result of first random number generation of random num between 1-12


if __name__ == "__main__":
    main()