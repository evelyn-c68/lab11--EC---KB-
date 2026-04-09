#https://github.com/evelyn-c68/lab11--EC---KB-.git
# Partner 1: Evelyn Chen
# Partner 2: Kaylee Bleeker

import unittest
from calculator import add, sub, mul, div, log, exp

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(0,0),0)
        self.assertEqual(add(-2,2),0)
        self.assertEqual(add(2,3),5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(4,2),2)
        self.assertEqual(sub(0,5),-5)
        self.assertEqual(sub(3,3),0)

    ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(1, 100),2)
        self.assertEqual(log(2,4),2)
        self.assertEqual(log(3,27),3)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            log(0,10) #base cannot 0
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()