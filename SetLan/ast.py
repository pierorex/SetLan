class Program(object):
    def __init__(self, statement):
        self.statement = statement
        
    def __repr__(self):
        indent = 4
        return 'Program\n' + indent*' ' + self.statement.__repr__(indent+4)


class Statement(object): pass


class Assign(Statement):
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression
    
    def __repr__(self, indent):
        return 'Assign\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n' + indent*' ' + 'value\n' + indent*' ' + self.expression.__repr__(indent+4)


class Block(Statement):
    def __init__(self, statements):
        self.statements = statements
        
    def __repr__(self, indent):
        return 'Block Start\n' + indent*' ' + self.statements.__repr__(indent+4) + '\n' + indent*' ' + 'Block End\n'


class Scan(Statement):
    def __init__(self, variable):
        self.variable = variable
        
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'


class Print(Statement):
    def __init__(self, print_list):
        self.print_list = print_list

    def __repr__(self, indent):
        return_string = 'Print\n'
        for element in self.print_list:
            return_string +=  + indent*' ' + element.__repr__(indent+4) + '\n'
        return return_string


class If(Statement):
    def __init__(self, expression, statement_true, statement_false=None):
        self.expression = expression
        self.statement_true = statement_true
        self.statement2_false = statement_false
    
    def __repr__(self, indent):
        return 'If\n' + indent*' ' + self.statement_true.__repr__(indent+4) + '\n' + indent*' ' + self.statement2_false.__repr__(indent+4) + '\n'


class For(Statement):
    def __init__(self, variable, order, statement):
        self.variable = variable
        self.order = order
        self.statement = statement

    def __repr__(self, indent):
        return 'For\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n' + indent*' ' + self.order + '\n' + indent*' ' + self.statement.__repr__(indent+4) + '\n'


class Repeat(Statement):
    def __init__(self, statement1, expression, statement2):
        self.statement1 = statement1
        self.expression = expression
        self.statement2 = statement2
    
    def __repr__(self, indent):
        if self.statement1:
            if self.statement2:
                return 'Repeat\n' + indent*' ' + self.statement1.__repr__(indent+4) + '\n' + indent*' ' + self.expression.__repr__(indent+4) + '\n' + self.statement2.__repr__(indent+4) + indent*' ' + '\n'
            else:
                return 'Repeat\n' + indent*' ' + self.statement1.__repr__(indent+4) + '\n' + indent*' ' + self.expression.__repr__(indent+4) + '\n'
        else:
            return 'Repeat\n' + indent*' ' + self.expression.__repr__(indent+4) + '\n' + indent*' ' + self.statement2.__repr__(indent+4) + '\n'
        
    
class Expression(object): pass


class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def __repr__(self, indent):
        return 'Variable\n' + indent*' ' + self.name.__repr__(indent+4) + '\n'
    

class Int(Expression):
    def __init__(self, value):
        self.value = value    
        
    def __repr__(self, indent):
        return 'Int\n' + indent*' ' + self.value + '\n'
    
    
class Bool(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self, indent):
        return 'Bool\n' + indent*' ' + self.value.__repr__(indent+4) + '\n'
    

class String(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self, indent):
        return 'String\n' + indent*' ' + self.value + '\n'


class BinOp(Expression): 
    def __init__(self, operator, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def __repr__(self, indent):
        return  self.class_name + '\n' + indent*' ' + self.operand1.__repr__(indent+4) + '\n' + self.operand2.__repr__(indent+4) + '\n'


class Plus(BinOp): pass

class Minus(BinOp): pass

class Times(BinOp): pass

class Div(BinOp): pass
    
class Mod(BinOp): pass
    
class PlusSet(BinOp): pass
    
class MinusSet(BinOp): pass

class TimesSet(BinOp): pass
    
class DivSet(BinOp): pass

class ModSet(BinOp): pass
    
class LessThan(BinOp): pass
        
class LessThanEq(BinOp): pass
        
class GreaterThan(BinOp): pass
    
class GreaterThanEq(BinOp): pass
        
class Equals(BinOp): pass
        
class NotEquals(BinOp): pass

class Union(BinOp): pass
    
class Difference(BinOp): pass
        
class Intersect(BinOp): pass
        
class And(BinOp): pass
        
class Or(BinOp): pass
        
class Contains(BinOp): pass
    

class UnaryOp(Expression):
    def __init__(self, operand):
        self.operand = operand

    def __repr__(self, indent):
        return self.class_name + '\n' + indent*' ' + self.operand.__repr__(indent+4) + '\n'
    
class Uminus(Expression): pass

class Not(Expression): pass
        
class Len(Expression): pass    
        
class MaxSet(Expression): pass
        
class MinSet(Expression): pass    