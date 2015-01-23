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

    def testCommentAndError(self):
        self.assertEqual(main('Tests/test5.txt'), open('Tests/answer5.txt','r').read())

    def testSample1(self):
        self.assertEqual(main('Tests/test6.txt'), open('Tests/answer6.txt','r').read())
    
    def testCommentAndError2(self):
        self.assertEqual(main('Tests/test7.txt'), open('Tests/answer7.txt','r').read())

    def testIfElse(self):
        self.assertEqual(main('Tests/test8.txt'), open('Tests/answer8.txt','r').read())
        
    def testOperators(self):
        self.assertEqual(main('Tests/test9.txt'), open('Tests/answer9.txt','r').read())
    
    def testSample2(self):
        self.assertEqual(main('Tests/test10.txt'), open('Tests/answer10.txt','r').read())
        
    def testBadVariables(self):
        self.assertEqual(main('Tests/test11.txt'), open('Tests/answer11.txt','r').read())

    def testJoins(self):
        self.assertEqual(main('Tests/test100.txt'), open('Tests/answer100.txt','r').read())

    def testAllContinue(self):
        self.assertEqual(main('Tests/test101.txt'), open('Tests/answer101.txt','r').read())    


if __name__ == '__main__':
    unittest.main()