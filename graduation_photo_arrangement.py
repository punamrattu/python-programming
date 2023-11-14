"""
It is the CFG Degree graduation day, and you are a photographer who has the task to take photos of our graduates.
The overall group has an even number of students, but Software graduates wear purple mortarboard hats and Data
graduates wear black mortarboard hats. In fact, exactly half of all students has purple hats and the other half has
black ones.

We need to arrange our students in two rows before taking any photos. Each row must contain the same
number of students and follow these precise guidelines:
• All Software students with purple hats must be in the same row.
• All Data students with black hats must be in the same row.
• Each student in the back row must be strictly taller than a student directly in front of them in the front row.
NB: you can assume that the overall group has at least two students.

We are given two input arrays:
• One contains the heights of all the students with purple hats
• Another one contains heights of all the students with black hats.
NB: these arrays will always be the same length and each height (number) will be a positive integer.

Please write a function that returns whether or not a graduation photo that follows the above strict guidelines can be taken.

Sample Input
purple_hats_heights = [5, 8, 1, 3, 4]
black_hats_heights = [6, 9, 2, 4, 5]

Sample Output
True    
"""



def check_photo(purple_hats_heights, black_hats_heights):
    """Check if a graduation photo follows specific guidelines.

    Arguments:
    purple_hats_heights (list): Heights of students with purple hats.
    black_hats_heights (list): Heights of students with black hats.

    Returns:
    bool: Indicates if the guidelines for the photo arrangement are met.
    """
    # Sort the heights of students
    purple_hats_heights.sort()
    black_hats_heights.sort()

    # Decide which row comes first based on the shortest student
    if purple_hats_heights[0] < black_hats_heights[0]:
        front_row = purple_hats_heights
        back_row = black_hats_heights
        print("FIRST ROW: PURPLE")
    else:
        front_row = black_hats_heights
        back_row = purple_hats_heights
        print("FIRST ROW: BLACK")

    # Compare the two rows based on student height to meet the guidelines
    for i in range(len(front_row)):
        if front_row[i] < back_row[i]:
            continue
        else:
            return False
    return True





    ## alternative solution:
    # compare heights at each index between the two lists, and append either True or False to a new list.
    # check if all the elements in the new list are the same and returns True if they are, False otherwise.
    #
    # compare = []
    # for i in range(len(front_row)):
    #     compare.append(front_row[i] < back_row[i])  # adds True/False to 'compare' list
    # result = all(element == compare[0] for element in compare)
    # if (result):
    #     return True
    # else:
    #     return False
