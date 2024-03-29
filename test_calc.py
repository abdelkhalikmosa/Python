import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-2, -2), -4)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-2, -2), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-2, -2), 4)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-2, -2), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)
        # self.assertRaises(ValueError, calc.divide, 105, 0)
        with self.assertRaises(ValueError):
            calc.divide(5, 0)


if __name__ == '__main__':
    unittest.main()

#  python -m unittest test_calc.py
#  python -B -m unittest test_calc.py # do not create cache files
