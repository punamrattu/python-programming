"""
Date Calculator Program

This Python script provides a simple utility for date manipulation, allowing users to either add a specified number of days to a given date or compare the difference in days between two provided dates.


Example walkthrough 1:

Please select one of the following options: add, compare
add

What is the date you want to add to? Please enter in DD/MM/YYYY format.
14/10/2000

How many days do you want to add?
56

The resultant date is 09/12/2000


Example walkthrough 2:

Please select one of the following options: add, compare
compare

Please give Date 1 in DD/MM/YYYY format.
14/10/2000

Please give Date 2 in DD/MM/YYYY format.
06/05/1999

There are 527 days between the given dates.



"""

import datetime
from datetime import datetime, timedelta

def add(str_date, days_to_add):
    date = datetime.strptime(str_date, "%d/%m/%Y")
    resultant_date = date + timedelta(days=int(days_to_add))
    resultant_date_formatted = resultant_date.strftime("%d/%m/%Y")
    print(f'The resultant date is {resultant_date_formatted}')

def compare(str_date1, str_date2):
    d1 = datetime.strptime(str_date1, "%d/%m/%Y")
    d2 = datetime.strptime(str_date2, "%d/%m/%Y")
    difference = d2 - d1
    print(f'There are {difference.days} days between the given dates.')

action = input('Please select one of the following options: add, compare ')

if action == 'add':
    str_date = input('What is the date you want to add to? Please enter in DD/MM/YYYY format.')
    days_to_add = input('How many days do you want to add? ')
    add(str_date, days_to_add)
else:
    str_date1 = input('Please give Date 1 in DD/MM/YYY format. ')
    str_date2 = input('Please give Date 2 in DD/MM/YYY format. ')
    compare(str_date1, str_date2)
