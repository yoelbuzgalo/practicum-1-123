import random

def roll_die(sides):
    """
    This function returns a random number between 1 to the total amount of sides of a die
    """
    random_num = random.randint(1, sides) # Generates a random integer number between 1 to the total amount of sides
    return random_num # Returns the random_num

def take_turn():
    """ Complete this function with your solution for Part C """

def main():
    """
    Main entry of this program
    """
    random.seed(37) # Setting seed to 37 to see output
    print(random.randint(1,12)) # This should print a result of 11, confirming that I can use this as a test number for my test module

if __name__ == "__main__":
    main()