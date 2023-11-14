string = 'wrtfawmnoonmz'

def generate_substrings(input_string):
    """Generate and print all possible substrings from the input string.

    Args:
    input_string (str): The input string.

    Returns:
    None
    """
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string)):
            substring = input_string[i : j + 1]
            print(substring)

generate_substrings(string)


