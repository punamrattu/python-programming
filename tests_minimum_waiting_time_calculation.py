"""
Tests for the 'min_waiting_time' function in the 'minimum_waiting_time_calculation.py' script.

These test cases aim to verify the accuracy of the 'min_waiting_time' function, which calculates the minimum total waiting time for patients awaiting their turn to see a doctor in an A&E department.

Each test_case_X function tests the 'min_waiting_time' function with different scenarios, using various lists of patient session durations. The 'expected' values represent the anticipated total waiting time for the provided patient lists.

Test Case List:
1. Verifies the minimum waiting time for a list with varying session durations.
2. Checks the waiting time for a list with uniform session durations.
3. Assesses waiting time for a list with varied session durations.
4. Assesses waiting time for a list with diverse and high-variance session durations.
5. Checks waiting time for a list with uniform short session durations to verify accurate computation.
6. Examines waiting time for a list with varied durations, including repetitions and high values.
7. Verifies the waiting time for a single patient, ensuring proper handling of single-element lists.
8. Assesses waiting time for a list with descending session durations to confirm accurate calculations.
9. Evaluates waiting time for a list with ascending session durations, ensuring consistent performance.
10. Evaluates waiting time for a list with repetitive session durations.

Each test asserts whether the 'min_waiting_time' function output matches the expected total waiting time.
"""


import unittest
from minimum_waiting_time_calculation import min_waiting_time

class TestProgram(unittest.TestCase):

    def test_case_1(self):
        patients = [3, 2, 1, 2, 6]
        expected = 17
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        patients = [2, 1, 1, 1]
        expected = 6
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        patients = [1, 2, 4, 5, 2, 1]
        expected = 23
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        patients = [25, 30, 2, 1]
        expected = 32
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        patients = [1, 1, 1, 1, 1]
        expected = 10
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        patients = [4, 3, 1, 1, 3, 2, 1, 8]
        expected = 45
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_7(self):
        patients = [2]
        expected = 0
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_8(self):
        patients = [5, 4, 3, 2, 1]
        expected = 20
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_9(self):
        patients = [1, 2, 3, 4, 5]
        expected = 20
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)

    def test_case_10(self):
        patients = [1, 1, 1, 4, 5, 6, 8, 1, 1, 2, 1]
        expected = 81
        actual = min_waiting_time(patients)
        self.assertEqual(actual, expected)
