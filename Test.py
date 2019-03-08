'''error system, test the functions in Proto.py'''

import unittest
import Proto   
import sys

class ArgTest(unittest.TestCase):

    self.lst = ['a', 'a', 'c', 'b']
    actual = self.assertEqual(Most_Common(lst))
    exepected = 'a'
    self.assertEqual(actual, exepected)

if __name__ == "__main__":
    unittest.main()




