"""
This script conducts test cases to evaluate the 'check_photo' function in 'graduation_photo_arrangement.py'. 

Test Cases:
1. Validates the arrangement when students in purple hats are shorter than those in black hats.
2. Ensures the function handles a scenario with only one student in each group.
3. Checks a case where both groups are arranged appropriately.
4. Verifies the function's response when all black-hat students are of the same height, rendering the arrangement impossible.
5. Examines a case where the height order between the groups does not meet the strict guidelines.
6. Tests an arrangement scenario with a shared height between purple and black hat students.
7. Assesses a case where the heights of purple and black hat students have the same order, rendering the arrangement infeasible.
8. Confirms an impossible arrangement when there are only two students in each group.
9. Checks a feasible arrangement when the tallest student in each group is not the same.
10. Revalidates a previous feasible scenario for redundancy and accuracy.

Each test case executes the 'check_photo' function with different inputs and checks the returned value against the expected output using 'assertEqual' from the 'unittest' module.
"""


import unittest
from graduation_photo_arrangement import check_photo


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        purple = [5, 8, 1, 3, 4]
        black = [6, 9, 2, 4, 5]
        expected = True
        actual = check_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        purple = [6]
        black = [6]
        expected = False
        actual = check_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        purple = [125]
        black = [126]
        expected = True
        actual = check_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        purple = [2, 3, 4, 5, 6]
        black = [1, 2, 3, 4, 5]
        expected = True
        actual = check_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        purple = [5, 6, 7, 2, 3, 1, 2, 3]
        black = [1, 1, 1, 1, 1, 1, 1, 1]
        expected = False
        actual = check_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        purple = [21, 5, 4, 4, 4, 4, 4, 4, 4]
        black = [19, 2, 4, 6, 2, 3, 1, 1, 4]
        expected = False
        actual = check_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_7(self):
        purple = [21, 5, 4, 4, 4, 4, 4, 4, 4]
        black = [19, 2, 3, 6, 2, 3, 1, 1, 3]
        expected = False
        actual = check_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_8(self):
        purple = [5, 4]
        black = [4, 5]
        expected = False
        actual = check_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_9(self):
        purple = [5, 4]
        black = [5, 6]
        expected = True
        actual = check_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_10(self):
        purple = [2, 3, 4, 5, 6]
        black = [1, 2, 3, 4, 5]
        expected = True
        actual = check_photo(purple, black)
        self.assertEqual(actual, expected)
