def human_years(dog_years):
    """
    This function returns calculated human years based off the American Kennel Club formula for dog years.
    """
    if dog_years <= 0:
        # If the dog_years parameter is less than or equal to 0, itll return 0 out of this function
        return 0
    elif dog_years == 1:
        # For 1 year only
        return 15
    elif dog_years == 2:
        # For 2 years only
        result = (15 + 9) # 15 for first year, plus 9 for additional year
        return result
    else:
        # For 3rd year and beyond
        result = (15+9) + ((dog_years - 2) * (5)) # It will add first 15 and 9 years, then for 3rd year and beyond itll multiply by 5
        return result

def main():
    """
    Main entry of this program
    """
    user_input = int(input("Enter dog's age in years: ")) # Prompts the user to enter dog's age in years
    print("Equivilent human years:", human_years(user_input)) # Calls human years function and prints the result to terminal

if __name__ == "__main__":
    main()