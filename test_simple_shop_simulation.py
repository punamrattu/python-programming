from unittest import TestCase, main
from simple_shop_simulation import validate_customer_input, is_within_budget, valid_attempt, MaxAttemptsExceededError


class TestShopping(TestCase):
    # Test the validation of customer input
    def test_validate_customer_input(self):
        shop = {'bag': 130, 'shoes': 70, 'belt': 45}

        # Valid customer input should be returned unchanged       
        expected = 'shoes'
        result = validate_customer_input(shop, 'shoes')
        self.assertEqual(expected, result)

        # Invalid customer input should raise a ValueError
        with self.assertRaises(ValueError):
            validate_customer_input(shop, 'socks')

    # Test if the chosen item is within budget
    def test_is_within_budget(self):
        shop = {'bag': 130, 'shoes': 70, 'belt': 45}
        budget = 100

        # An affordable item should return True
        result = is_within_budget(budget, shop, 'belt')
        self.assertTrue(result)

        # An unaffordable item should return False
        result = is_within_budget(budget, shop, 'bag')
        self.assertFalse(result)

    # Test the limit of attempts by the customer
    def test_valid_attempt(self):
        # No exception should be raised when the number of attempts is less than max_attempts
        with self.assertRaises(MaxAttemptsExceededError):
            valid_attempt(2, 3)

        # An exception should be raised when the number of attempts is more than max_attempts
        with self.assertRaises(MaxAttemptsExceededError):
            valid_attempt(4, 3)
