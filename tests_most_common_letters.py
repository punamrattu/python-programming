"""
This script contains unit tests for the 'most_common_three' function in the 'most_common_letters.py' program.

Test Cases:
1. Verifies the identification of the three most common letters in a valid sentence with multiple distinct letters, expecting a specific result.
2. Assesses the handling of an invalid sentence consisting only of spaces, which should raise the 'NoMostCommonThree' exception.
3. Checks an edge case with a sentence that has four letters, but only two unique ones, aiming to trigger the 'NoMostCommonThree' exception.

Each test case validats the 'most_common_three' function's output against the expected results or raised exceptions.
"""


import unittest
from most_common_letters import most_common_three, NoMostCommonThree


class TestPangram(unittest.TestCase):
    # testing a valid sentence that has at least 3 letters to see if it returns the expected result
    def test_most_common_three_valid(self):
        sentence = "hello world"
        expected = ['l', 'o', 'd']
        self.assertEqual(expected, most_common_three(sentence))

    # testing an invalid sentence that has only spaces therefore shouldn't be considered
    def test_most_common_three_invalid(self):
        with self.assertRaises(NoMostCommonThree):
            most_common_three(" ")

    # testing a sentence that has four letters, but only 2 are unique therefore should error
    def test_most_common_three_edge_case(self):
        with self.assertRaises(NoMostCommonThree):
            most_common_three("abab")
