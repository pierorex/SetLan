import unittest
from setlan import *

class TestSuite(unittest.TestCase):
    def testSimple(self):
        self.assertEqual(main("test1.txt"), open("answer1.txt",'r').read())