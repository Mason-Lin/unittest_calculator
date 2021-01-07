import unittest

from calculator import Calculator


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_positive_inter_sum(self):
        self.sum_should_be(3, 1, 2)

    def sum_should_be(self, expected, first, second):
        sum = self.calculator.sum(first, second)
        self.assertEqual(expected, sum)


if __name__ == '__main__':
    unittest.main()
