from time import sleep
import inc_dec    # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):

    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(3), 2)

    def test_increment(self):
        self.assertEqual(inc_dec.increment(3),2)

if __name__ == '__main__':
    unittest.main()
else:
    sleep(5)