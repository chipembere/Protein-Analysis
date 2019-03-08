'''error system'''

import unittest
import Proto   
import sys

class ArgTest(unittest.TestCase):
    xml_path = sys.argv[1]
    function_word = sys.argv[2]

    def test_args(self):
        print('argument 1: ', self.xml_path)
        print('argument 2: ', self.function_word)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        MyTest.xml_path = sys.argv.pop()
        MyTest.function_word = sys.argv.pop()
    unittest.main()




