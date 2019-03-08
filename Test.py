'''error system, test the functions in Proto.py'''

import unittest
from Proto import Most_Common
#import sys

class ArgTest(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_m_s(self):
        lst = ['a', 'a', 'c', 'b']
        actual = Most_Common(lst)
        exepected = 'a'
        self.assertEqual(actual, exepected)

if __name__ == "__main__":
    unittest.main()




