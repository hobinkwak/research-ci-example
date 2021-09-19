import unittest

import main

class MainTest(unittest.TestCase):
    def test_helloworld(selfself):
        ret = main.hellow('test')
        self.assertEqual(ret, "Hellow World: hobin!")

if __name__ == '__main__':
    unittest.main()