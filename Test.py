'''error system, test the functions in Proto.py'''

import unittest
from Proto import Most_Common
#import sys

class ArgTest(unittest.TestCase):
    
    def setUp(self):
        lst = ['a', 'a', 'c', 'b']
        actual = self.assertEqual(Most_Common(lst))
        exepected = 'a'
        self.assertEqual(actual, exepected)

    #def 

if __name__ == "__main__":
    unittest.main()




