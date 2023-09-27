START_VALUE = ord("A")

def convert_to_upper(char):
    """ 
    This function converts lower case characters to upper case characters
    """
    char_ascii_value = ord(char) - 65
    selected_upper_case = chr(START_VALUE + char_ascii_value)
    return selected_upper_case

def main():
    print(convert_to_upper("a"))

main()