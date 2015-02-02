import unittest
from lexer import mainLexer
#from parser import mainParser

class LexerTestSuite(unittest.TestCase):
    def testSimple(self):
        self.assertEqual(mainLexer('Tests/test1.txt'), open('Tests/answer1.txt','r').read())

    def testString(self):
        self.assertEqual(mainLexer('Tests/test2.txt'), open('Tests/answer2.txt','r').read())

    def testString2(self):
        self.assertEqual(mainLexer('Tests/test3.txt'), open('Tests/answer3.txt','r').read())

    def testSimpleError(self):
        self.assertEqual(mainLexer('Tests/test4.txt'), open('Tests/answer4.txt','r').read())

    def testCommentAndError(self):
        self.assertEqual(mainLexer('Tests/test5.txt'), open('Tests/answer5.txt','r').read())

    def testSample1(self):
        self.assertEqual(mainLexer('Tests/test6.txt'), open('Tests/answer6.txt','r').read())
    
    def testCommentAndError2(self):
        self.assertEqual(mainLexer('Tests/test7.txt'), open('Tests/answer7.txt','r').read())

    def testIfElse(self):
        self.assertEqual(mainLexer('Tests/test8.txt'), open('Tests/answer8.txt','r').read())
        
    def testOperators(self):
        self.assertEqual(mainLexer('Tests/test9.txt'), open('Tests/answer9.txt','r').read())
    
    def testSample2(self):
        self.assertEqual(mainLexer('Tests/test10.txt'), open('Tests/answer10.txt','r').read())
        
    def testBadVariables(self):
        self.assertEqual(mainLexer('Tests/test11.txt'), open('Tests/answer11.txt','r').read())

    def testJoins(self):
        self.assertEqual(mainLexer('Tests/test100.txt'), open('Tests/answer100.txt','r').read())

    def testAllContinue(self):
        self.assertEqual(mainLexer('Tests/test101.txt'), open('Tests/answer101.txt','r').read())    

    def testOperatorsWithoutSpaces(self):
        self.assertEqual(mainLexer('Tests/test12.txt'), open('Tests/answer12.txt','r').read())
        
    def testSetMinMaxContains(self):
        self.assertEqual(mainLexer('Tests/test13.txt'), open('Tests/answer13.txt','r').read())

    def testEscapeBackS(self):
        self.assertEqual(mainLexer('Tests/testCarlitos.txt'), open('Tests/answerCarlitos.txt','r').read())



class ParserTestSuite(unittest.TestCase):
    def testEscapeBackS(self):
        self.assertEqual(mainLexer('Tests/testCarlitos.txt'), open('Tests/answerCarlitos.txt','r').read())

if __name__ == '__main__':
    unittest.main()
