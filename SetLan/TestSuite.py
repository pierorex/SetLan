import unittest
from setlan import main

class TestSuite(unittest.TestCase):
    def testSimple(self):
        self.assertEqual(main('Tests/test1.txt'), open('Tests/answer1.txt','r').read())
        
    def testString(self):
        self.assertEqual(main('Tests/test2.txt'), open('Tests/answer2.txt','r').read())
    
    def testString2(self):
        self.assertEqual(main('Tests/test3.txt'), open('Tests/answer3.txt','r').read())
        
    def testSimpleError(self):
        self.assertEqual(main('Tests/test4.txt'), open('Tests/answer4.txt','r').read())
    
if __name__ == '__main__':
    unittest.main()