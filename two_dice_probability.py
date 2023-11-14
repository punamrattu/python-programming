"""
This program simulates 100 rolls of two dice and records the outcomes to determine the frequency of each possible total, ranging from 2 to 12. By calculating these frequencies, the program then estimates the probability of obtaining each specific total. Users can select a target number representing the total outcome from both dice, and the program provides the probability of achieving that selected number.

For example:
● If 1 was the input, the output would be: The chance of you getting 1 is 0%
● If 7 was the input, the output would be: The chance of you getting 7 is 12%
"""


import random

roll = 1

# Dictionary to store the count of each possible outcome
result_count = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

def count(n):
    # Increment the count for the given outcome
    result_count[n] = result_count[n] + 1

while roll <= 100:
    # Simulate rolling two dice and summing the outcomes
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    result = dice1 + dice2
    count(result)
    roll += 1

# Ask the user to input the number they're trying to get
user_number = input('You have 2 dice. What number (total from both dice) are you trying to get? ')

# Get the probability of the user's input number based on the simulated rolls
probability = result_count[int(user_number)]

# Display the probability of getting the user's number
print(f'The chance of you getting {user_number} is {probability}%')

