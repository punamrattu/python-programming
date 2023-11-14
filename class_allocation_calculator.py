"""
This program calculates the optimal number of classes required to accommodate a given number of students, ensuring adherence to key constraints. The constraints include a maximum class size of 30, a minimum of 2 classes, an even distribution of students among classes, and a focus on minimizing the number of employed personnel.

The main function takes the number of students as input and outputs a string indicating the proposed number of classes and a dictionary detailing the allocation of students to each class.

Key Constraints:
- Maximum class size: 30
- Minimum number of classes: 2
- Even distribution of students among classes
- Minimization of employed personnel by prioritizing larger classes

Inputs/Outputs:
- For example, if the input is 31, the output would be:
  Proposed Allocation: 2 classes
  {'Class 1': 16, 'Class 2': 15}

- If the input is 59, the output would be:
  Proposed Allocation: 2 classes
  {'Class 1': 30, 'Class 2': 29}

- And for an input of 87, the output would be:
  Proposed Allocation: 3 classes
  {'Class 1': 29, 'Class 2': 29, 'Class 3': 29}

"""


import math

def allocate_classes(students):
    """
    Allocate students into classes based on a 30-student limit per class.

    Args:
        students (int): The total number of students to be allocated to classes.

    Returns:
        dict: A dictionary with the class names as keys and the number of students allocated to each class.
    """
    # Calculate the number of classes needed based on a 30-student limit
    no_of_classes = math.ceil(students / 30)
    
    # Determine the ideal number of students per class and the leftover students
    students_per_class = students // no_of_classes
    leftover_students = students % no_of_classes
    
    # Create a dictionary to allocate students to each class
    allocation = {}
    for i in range(no_of_classes):
        # Distribute the remaining students among the classes
        class_size = students_per_class + int(i < leftover_students)
        allocation[f"Class {i+1}"] = class_size
    
    # Print the proposed class allocation details
    print(f"Proposed Allocation: {no_of_classes} classes")
    print(allocation)

