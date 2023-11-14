"""
You work as a primary school teacher and are teaching numbers by showing how they are composed of units of ten and one. Write a program for students to play with to understand this concept. You will be asking for them to enter numbers between 1 and 25 (they haven’t gone higher than that!), so you do not need to consider bigger numbers. The function needs to print to the screen and the message must be grammatically correct and in the format shown below.
"""


# Prompt the user to enter a number between 1-25
number = input('What is your number? ')

# Ensure a single-digit number has a leading zero
number = '%02d' % int(number)

# Split the input number into individual digits
digits = [int(i) for i in str(number)]

# Define text formats based on the number's digits
if digits[0] == 1:
    ten_format = 'Ten'
else:
    ten_format = 'Tens'

if digits[1] == 1:
    one_format = 'One'
else:
    one_format = 'Ones'

# Create a dictionary mapping digits to their word representation
num_words = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 6: 'Six', 5: 'Five', 7: 'Seven', 8: 'Eight', 9: 'Nine'}

# Convert the digits into word form
def convert(n):
    return num_words[n]

# Retrieve word representations for the two digits
first_digit = convert(digits[0])
second_digit = convert(digits[1])

# Print the output in a formatted way
print(f"{first_digit} {ten_format}, {second_digit} {one_format}")

