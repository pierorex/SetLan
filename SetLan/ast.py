class Program:
    def __init__(self, statement):
        self.statement = statement
        
    def __repr__(self):
        indent = 4
        return 'Program\n' + indent*' ' + self.statement.__repr__(indent+4)


class Statement: pass


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
                return 'Repeat\n' + indent*' ' + self.statement1.__repr__(indent+4)

"""class While(Statement):
    def __init__(self, condition, statement):
        self.condition = condition
        self.statement = statement

    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'"""
    
    
class Expression: pass


class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    

class Int(Expression):
    def __init__(self, value):
        self.value = value    
        
    def __repr__(self, indent):
        return 'Int\n' + indent*' ' + self.value + '\n'
    
    
class Bool(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    

class String(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self, indent):
        return 'String\n' + indent*' ' + self.value + '\n'


class Plus(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator

    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    

class Minus(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator

    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'


class Times(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator

    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    

class Div(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator

    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    

class Mod(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator

    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
    
class PlusSet(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator

    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    

class MinusSet(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator

    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    

class TimesSet(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
    
class DivSet(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator

    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    

class ModSet(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
   
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
    
class LessThan(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
        
class LessThanEq(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right   
        self.operator = operator
   
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
        
        
class GreaterThan(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
    
class GreaterThanEq(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
        
class Equals(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
        
class NotEquals(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
        
class Union(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right      
        self.operator = operator  
   
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
    
class Difference(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right      
        self.operator = operator   
        
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
        
class Intersect(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
        
class And(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
        
class Or(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator
        
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
        
class Contains(Expression):
    def __init__(self, operator, left, right):
        self.left = left
        self.right = right
        self.operator = operator

    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
    
class Uminus(Expression):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
        
class Not(Expression):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand
        
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
        
class Len(Expression):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand
        
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
        
class MaxSet(Expression):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand
        
    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    
        
class MinSet(Expression):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def __repr__(self, indent):
        return 'Scan\n' + indent*' ' + self.variable.__repr__(indent+4) + '\n'
    