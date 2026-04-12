#https://github.com/evelyn-c68/lab11--EC---KB-.git
# Partner 1: Evelyn Chen
# Partner 2: Kaylee Bleeker

import unittest
from calculator import add, subtract, mul, div, logarithm, exp, hypotenuse, square_root

class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(0,0),0)
        self.assertEqual(add(-2,2),0)
        self.assertEqual(add(2,3),5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(4,2),2)
        self.assertEqual(subtract(0,5),-5)
        self.assertEqual(subtract(3,3),0)


    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self):
        self.assertEqual(div(2, 1), 2)
        self.assertEqual(div(-6, 2), -3)
        with self.assertRaises(ZeroDivisionError):
            div(6, 0)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def test_logarithm(self):
        with self.assertRaises(ValueError):
            logarithm(-1, 10)
        with self.assertRaises(ValueError):
            logarithm(1, 100)
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(0,10) #base cannot 0

    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(-1, 10)
        with self.assertRaises(ValueError):
            logarithm(1, 100)
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(4), 2.0)
        self.assertAlmostEqual(square_root(9), 3.0)
        with self.assertRaises(ValueError):
            square_root(-4)


# Do not touch this
if __name__ == "__main__":
    unittest.main()