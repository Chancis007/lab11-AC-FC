# https://github.com/Chancis007/lab11-AC-FC.git
# Partner 1: Anna Chandler
# Partner 2: Francis Chan

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 2), 1)


    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-1, -1), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,6),18)
        self.assertEqual(mul(5, -10),-50)
        self.assertEqual(mul(-3, -8),24)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(4,20),5)
        self.assertEqual(div(-3, 15), -5)
        self.assertEqual(div(20, 0), 0)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(8, 2), 3)
        self.assertEqual(logarithm(100, 10), 2)
        self.assertEqual(logarithm(5, 5), 1)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 10)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,5)
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3,4),5.0)
        self.assertAlmostEqual(hypotenuse(0,5),5.0)
        self.assertAlmostEqual(hypotenuse(-3,4),5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-16)
        self.assertAlmostEqual(square_root(0.01),0.1)
        self.assertAlmostEqual(square_root(25),5)
        self.assertAlmostEqual(square_root(0),0.0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()