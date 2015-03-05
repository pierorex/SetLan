import unittest
from parser import mainFlags

class LexerTestSuite(unittest.TestCase):
    def testSimple(self):
        self.assertEqual(mainFlags(['','Tests/test1.txt','-t']), open('Tests/answer1.txt','r').read())
    def testString(self):
        self.assertEqual(mainFlags(['','Tests/test2.txt','-t']), open('Tests/answer2.txt','r').read())
    def testString2(self):
        self.assertEqual(mainFlags(['','Tests/test3.txt','-t']), open('Tests/answer3.txt','r').read())
    def testSimpleError(self):
        self.assertEqual(mainFlags(['','Tests/test4.txt','-t']), open('Tests/answer4.txt','r').read())
    def testCommentAndError(self):
        self.assertEqual(mainFlags(['','Tests/test5.txt','-t']), open('Tests/answer5.txt','r').read())
    def testSample1(self):
        self.assertEqual(mainFlags(['','Tests/test6.txt','-t']), open('Tests/answer6.txt','r').read())
    def testCommentAndError2(self):
        self.assertEqual(mainFlags(['','Tests/test7.txt','-t']), open('Tests/answer7.txt','r').read())
    def testIfElse(self):
        self.assertEqual(mainFlags(['','Tests/test8.txt','-t']), open('Tests/answer8.txt','r').read())
    def testOperators(self):
        self.assertEqual(mainFlags(['','Tests/test9.txt','-t']), open('Tests/answer9.txt','r').read())
    def testSample2(self):
        self.assertEqual(mainFlags(['','Tests/test10.txt','-t']), open('Tests/answer10.txt','r').read())
    def testBadVariables(self):
        self.assertEqual(mainFlags(['','Tests/test11.txt','-t']), open('Tests/answer11.txt','r').read())
    def testJoins(self):
        self.assertEqual(mainFlags(['','Tests/test100.txt','-t']), open('Tests/answer100.txt','r').read())
    def testAllContinue(self):
        self.assertEqual(mainFlags(['','Tests/test101.txt','-t']), open('Tests/answer101.txt','r').read())    
    def testOperatorsWithoutSpaces(self):
        self.assertEqual(mainFlags(['','Tests/test12.txt','-t']), open('Tests/answer12.txt','r').read())
    def testSetMinMaxContains(self):
        self.assertEqual(mainFlags(['','Tests/test13.txt','-t']), open('Tests/answer13.txt','r').read())
    def testEscapeBackS(self):
        self.assertEqual(mainFlags(['','Tests/testCarlitos.txt','-t']), open('Tests/answerCarlitos.txt','r').read())


class ParserTestSuite(unittest.TestCase):
    def testSimple1(self):
        self.assertEqual(mainFlags(['','Tests/testSimple1.txt','-a']), open('Tests/answerSimple1.txt','r').read())
    def testSimple2(self):
        self.assertEqual(mainFlags(['','Tests/testSimple2.txt','-a']), open('Tests/answerSimple2.txt','r').read())
    def testSimpleError(self):
        self.assertEqual(mainFlags(['','Tests/testSimpleError.txt','-a']), open('Tests/answerSimpleError.txt','r').read())
    def testIfThen(self):
        self.assertEqual(mainFlags(['','Tests/testIfThen.txt','-a']), open('Tests/answerIfThen.txt','r').read())
    def testIfThenElse(self):
        self.assertEqual(mainFlags(['','Tests/testIfThenElse.txt','-a']), open('Tests/answerIfThenElse.txt','r').read())
    def testAssign(self):
        self.assertEqual(mainFlags(['','Tests/testAssign.txt','-a']), open('Tests/answerAssign.txt','r').read())
    def testUsing(self):
        self.assertEqual(mainFlags(['','Tests/testUsing.txt','-a']), open('Tests/answerUsing.txt','r').read())
    def testUsingTwoDataTypes(self):
        self.assertEqual(mainFlags(['','Tests/testUsingTwoDataTypes.txt','-a']), open('Tests/answerUsingTwoDataTypes.txt','r').read())
    def testUsingThreeDataTypes(self):
        self.assertEqual(mainFlags(['','Tests/testUsingThreeDataTypes.txt','-a']), open('Tests/answerUsingThreeDataTypes.txt','r').read())
    def testScan(self):
        self.assertEqual(mainFlags(['','Tests/testScan.txt','-a']), open('Tests/answerScan.txt','r').read())
    def testCurlySet(self):
        self.assertEqual(mainFlags(['','Tests/testCurlySet.txt','-a']), open('Tests/answerCurlySet.txt','r').read())
    def testAssignErrors(self):
        self.assertEqual(mainFlags(['','Tests/testAssignErrors.txt','-a']), open('Tests/answerAssignErrors.txt','r').read())
    def testError(self):
        self.assertEqual(mainFlags(['','Tests/testError.txt','-a']), open('Tests/answerError.txt','r').read())
    def testError2(self):
        self.assertEqual(mainFlags(['','Tests/testError2.txt','-a']), open('Tests/answerError2.txt','r').read())
    def testIf2(self):
        self.assertEqual(mainFlags(['','Tests/testIf2.txt','-a']), open('Tests/answerIf2.txt','r').read())
    def testIfElse2(self):
        self.assertEqual(mainFlags(['','Tests/testIfElse2.txt','-a']), open('Tests/answerIfElse2.txt','r').read())
    def testSimpleFor(self):
        self.assertEqual(mainFlags(['','Tests/testSimpleFor.txt','-a']), open('Tests/answerSimpleFor.txt','r').read())
    def testSimpleForMultiOperations(self):
        self.assertEqual(mainFlags(['','Tests/testSimpleForMultiOperations.txt','-a']), open('Tests/answerSimpleForMultiOperations.txt','r').read())
    def testSimpleForInvertedDirection(self):
        self.assertEqual(mainFlags(['','Tests/testSimpleForInvertedDirection.txt','-a']), open('Tests/answerSimpleForInvertedDirection.txt','r').read())
    def testSimpleWhile(self):
        self.assertEqual(mainFlags(['','Tests/testSimpleWhile.txt','-a']), open('Tests/answerSimpleWhile.txt','r').read())
    def testNestedOperation(self):
        self.assertEqual(mainFlags(['','Tests/testNestedOperation.txt','-a']), open('Tests/answerNestedOperation.txt','r').read())
    def testRepeatWhileDo(self):
        self.assertEqual(mainFlags(['','Tests/testRepeatWhileDo.txt','-a']), open('Tests/answerRepeatWhileDo.txt','r').read())
    def testRepeatWhile(self):
        self.assertEqual(mainFlags(['','Tests/testRepeatWhile.txt','-a']), open('Tests/answerRepeatWhile.txt','r').read())
    def testNestedOperation2(self):
        self.assertEqual(mainFlags(['','Tests/testNestedOperation2.txt','-a']), open('Tests/answerNestedOperation2.txt','r').read())
    def testNestedOperationSets(self):
        self.assertEqual(mainFlags(['','Tests/testNestedOperationSets.txt','-a']), open('Tests/answerNestedOperationSets.txt','r').read())
    def testNestedOperationSets2(self):
        self.assertEqual(mainFlags(['','Tests/testNestedOperationSets2.txt','-a']), open('Tests/answerNestedOperationSets2.txt','r').read())
    def testFor(self):
        self.assertEqual(mainFlags(['','Tests/testFor.txt','-a']), open('Tests/answerFor.txt','r').read())
    def testSetsOperators(self):
        self.assertEqual(mainFlags(['','Tests/testSetsOperators.txt','-a']), open('Tests/answerSetsOperators.txt','r').read())
    def testIfElse3(self):
        self.assertEqual(mainFlags(['','Tests/testIfElse3.txt','-a']), open('Tests/answerIfElse3.txt','r').read())
    def testIfError1(self):
        self.assertEqual(mainFlags(['','Tests/testIfError1.txt','-a']), open('Tests/answerIfError1.txt','r').read())
    def testIfError2(self):
        self.assertEqual(mainFlags(['','Tests/testIfError2.txt','-a']), open('Tests/answerIfError2.txt','r').read())
    def testForInsideFor(self):
        self.assertEqual(mainFlags(['','Tests/testForInsideFor.txt','-a']), open('Tests/answerForInsideFor.txt','r').read())
    def testAll(self):
        self.assertEqual(mainFlags(['','Tests/testAll.txt','-a']), open('Tests/answerAll.txt','r').read())
    def testPrecedenceOperators(self):
        self.assertEqual(mainFlags(['','Tests/testPrecedenceOperators.txt','-a']), open('Tests/answerPrecedenceOperators.txt','r').read())
    def testAssociativeOperatorsSets(self):
        self.assertEqual(mainFlags(['','Tests/testAssociativeOperatorsSets.txt','-a']), open('Tests/answerAssociativeOperatorsSets.txt','r').read())
    def testFibonacci(self):
        self.assertEqual(mainFlags(['','Tests/testFibonacci.txt','-a']), open('Tests/answerFibonacci.txt','r').read())
    def testWhileInsideRepeat(self):
        self.assertEqual(mainFlags(['','Tests/testWhileInsideRepeat.txt','-a']), open('Tests/answerWhileInsideRepeat.txt','r').read())
    def testSetZeroElement(self):
        self.assertEqual(mainFlags(['','Tests/testSetZeroElement.txt','-a']), open('Tests/answerSetZeroElement.txt','r').read())
    def testEmptySet(self):
        self.assertEqual(mainFlags(['','Tests/testEmptySet.txt','-a']), open('Tests/answerEmptySet.txt','r').read())


class StaticCheckerTestSuite(unittest.TestCase):
    def testStaticEmptySet(self):
        self.assertEqual(mainFlags(['','Tests/testStaticEmptySet.txt','-s']), open('Tests/answerStaticEmptySet.txt','r').read())
    def testTwoSeparateScopes(self):
        self.assertEqual(mainFlags(['','Tests/testTwoSeparateScopes.txt','-s']), open('Tests/answerTwoSeparateScopes.txt','r').read())
    def testOneRedeclaredVariable(self):
        self.assertEqual(mainFlags(['','Tests/testOneRedeclaredVariable.txt','-s']), open('Tests/answerOneRedeclaredVariable.txt','r').read())
    def testThreeRedeclaredVariables(self):
        self.assertEqual(mainFlags(['','Tests/testThreeRedeclaredVariables.txt','-s']), open('Tests/answerThreeRedeclaredVariables.txt','r').read())
    def testSameVariableTwoScopes(self):
        self.assertEqual(mainFlags(['','Tests/testSameVariableTwoScopes.txt','-s']), open('Tests/answerSameVariableTwoScopes.txt','r').read())
    def testForScope(self):
        self.assertEqual(mainFlags(['','Tests/testForScope.txt','-s']), open('Tests/answerForScope.txt','r').read())
    def testSimpleTypeChecking(self):
        self.assertEqual(mainFlags(['','Tests/testSimpleTypeChecking.txt','-s']), open('Tests/answerSimpleTypeChecking.txt','r').read())
    def testDifferentiatingScopes(self):
        self.assertEqual(mainFlags(['','Tests/testDifferentiatingScopes.txt','-s']), open('Tests/answerDifferentiatingScopes.txt','r').read())
    def testIfTypeCheck(self):
        self.assertEqual(mainFlags(['','Tests/testIfTypeCheck.txt','-s']), open('Tests/answerIfTypeCheck.txt','r').read())
    def testScanChecker(self):
        self.assertEqual(mainFlags(['','Tests/testScanChecker.txt','-s']), open('Tests/answerScanChecker.txt','r').read())
    def testForTypeCheck(self):
        self.assertEqual(mainFlags(['','Tests/testForTypeCheck.txt','-s']), open('Tests/answerForTypeCheck.txt','r').read())
    def testRepeatTypeCheck(self):
        self.assertEqual(mainFlags(['','Tests/testRepeatTypeCheck.txt','-s']), open('Tests/answerRepeatTypeCheck.txt','r').read())
    def testMediumProgramScopes(self):
        self.assertEqual(mainFlags(['','Tests/testMediumProgramScopes.txt','-s']), open('Tests/answerMediumProgramScopes.txt','r').read())


class DynamicCheckerTestSuite(unittest.TestCase):
    def testInterpretOps(self):
        self.assertEqual(mainFlags(['','Tests/testInterpretOps.txt']), open('Tests/answerInterpretOps.txt','r').read())
    def testInterpretIf(self):
        self.assertEqual(mainFlags(['','Tests/testInterpretIf.txt']), open('Tests/answerInterpretIf.txt','r').read())
    def testInterpretFor(self):
        self.assertEqual(mainFlags(['','Tests/testInterpretFor.txt']), open('Tests/answerInterpretFor.txt','r').read())


if __name__ == '__main__':
    unittest.main()

