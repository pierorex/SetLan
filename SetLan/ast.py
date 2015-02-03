# To set indentation automatically
def indent(level):
    return "    " * level


class Program:
    def __init__(self, statement):
        self.statement = statement


class Statement: pass


class Assign(Statement):
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression


class Block(Statement):
    def __init__(self, statements):
        self.statements = statements


class Scan(Statement):
    def __init__(self, variable):
        self.variable = variable


class Print(Statement):
    def __init__(self, elements):
        self.elements = elements


class If(Statement):
    def __init__(self, condition, then_st, else_st=None):
        self.condition = condition
        self.then_st = then_st
        self.else_st = else_st


class For(Statement):
    def __init__(self, variable, in_range, statement):
        self.variable = variable
        self.in_range = in_range
        self.statement = statement


class Repeat(Statement):
    def __init__(self, condition, statement):
        self.condition = condition
        self.statement = statement
        

class While(Statement):
    def __init__(self, condition, statement):
        self.condition = condition
        self.statement = statement


class Expression: pass


class Variable(Expression):
    def __init__(self, name):
        self.name = name


class Int(Expression):
    def __init__(self, value):
        self.value = value


class Bool(Expression):
    def __init__(self, value):
        self.value = value


class String(Expression):
    def __init__(self, value):
        self.value = value


class Plus(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator


class Minus(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator


class Times(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator


class Div(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator


class Mod(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator


class PlusSet(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator


class MinusSet(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator


class TimesSet(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        

class DivSet(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator


class ModSet(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
   
   
class LessThan(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
        
class LessThanEq(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right   
        self.operator = operator
   
        
class GreaterThan(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
        
class GreaterThanEq(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
        
class Equals(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
        
class NotEquals(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
        
class Union(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right      
        self.operator = operator  
   

class Difference(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right      
        self.operator = operator   
        
        
class Intersect(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
        
class And(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
        
class Or(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
        
class Contains(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator


class Uminus(Expression):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

        
class Not(Expression):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand
        
        
class Len(Expression):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand
        
        
class MaxSet(Expression):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand
        
        
class MinSet(Expression):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand