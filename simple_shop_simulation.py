"""
Simple Shop Program

This program simulates a customer shopping experience, managing their budget and purchase attempts. It employs exception handling with try/except/else blocks and aims for at least two keyword uses (e.g., try/except, raise).

Tasks:
1. Create a dictionary listing at least 3 items with their prices. Ensure one item costs more than £100.
2. The customer has £100 available for shopping.
3. Upon welcoming the customer, display the available items and their prices, providing an 'exit' option.
4. Handle user input, raising a ValueError for invalid entries.
5. If the customer can afford the chosen item, acknowledge the purchase with a specific message.
6. Prompt the customer out of the shop, terminating the program.
7. In case of insufficient funds, track the attempts and offer the customer the chance to add more money.
8. Limit the purchase attempts to a maximum of 3. Exceeding attempts triggers a custom error, leading to the customer exiting the shop.

"""

# Custom exception for exceeding allowed number of attempts
class MaxAttemptsExceededError(ValueError):
    pass


# Function to validate customer input
def validate_customer_input(shop, customer_input):
    if customer_input not in shop:
        raise ValueError("Invalid option! Valid options are: bag, shoes, belt.")
    return customer_input


# Function to check if chosen item is within budget
def is_within_budget(budget, shop, customer_input):
    return shop.get(customer_input, 0) <= budget


# Function to limit the number of attempts by the customer
def valid_attempt(attempt, max_attempts):
    if attempt >= max_attempts:
        raise MaxAttemptsExceededError("You have exceeded the maximum number of attempts. Goodbye!")
    else:
        return True


# Function simulating the shopping experience
def shop_simulation():
    shop = {'bag': 130, 'shoes': 70, 'belt': 45}
    budget = 100
    max_attempts = 3
    attempt = 0

    print('Welcome to the shop!')
    print('Here are the available items and their prices:')
    for item, price in shop.items():
        print(f"{item}: £{price}")

    while True:
        customer_input = input(
            'Please type in the item you would like to purchase. Alternatively, if you would like to leave the shop, '
            'type exit: ')

        if customer_input != 'exit':
            try:
                customer_input = validate_customer_input(shop, customer_input)
            except ValueError as e:
                print(f"{e}")
                quit()
        else:
            print("Goodbye!")
            quit()

        try:
            valid_attempt(attempt, max_attempts)
        except MaxAttemptsExceededError as e:
            print(f"{e}")
            break
        else:
            if is_within_budget(budget, shop, customer_input):
                print(f'Thank you for buying {customer_input}. Goodbye!')
                break
            else:
                attempt += 1
                top_up_amount = input('You cannot afford this item! Would you like to top up your budget? '
                                      'If yes, type amount, if not then type "no" ')
                if top_up_amount != 'no':
                    budget += float(top_up_amount)
                else:
                    print("Goodbye!")
                    break

