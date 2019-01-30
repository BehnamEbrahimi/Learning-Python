import unittest
import calc # we must import the module that we want to test


class TestCalc(unittest.TestCase): # in order to create test cases we should create a class which inherents from TestCase

    def test_add(self): # the name of the methods must start by start_
        self.assertEqual(calc.add(10, 5), 15) # there are methods in unittest like assertEqual (==), assertNotEqual (!=), assertTrue, assertIsNotNone... see the documentation
        self.assertEqual(calc.add(-1, 1), 0) # checking edge cases
        self.assertEqual(calc.add(-1, -1), -2) # the goal is not writing as many test cases as possible but good ones

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5) # to spot // floor division

        self.assertRaises(ValueError, calc.divide, 10, 0) # to check if the function raise an expected exception or not. the second argument must be the function without () and the parameter of that function must follow after

        with self.assertRaises(ValueError): # this mehtod is exactly as above by using context manager. in this way, the method is called as it should be called
            calc.divide(10, 0)


if __name__ == '__main__': # by this, we can run the test directly from this file, not by calling unittest as our main file and passing this file as module
    unittest.main()
