static_checking_errors = ''


class Program(object):
    def __init__(self, statement):
        self.statement = statement
        
    def repr(self):
        indent = 4
        if self.statement:
            sta = self.statement.__repr__() if not getattr(self.statement,'repr',None) else self.statement.repr(indent+4) 
            return 'Program\n' + indent*' ' + sta
        else:
            return 'Program\n'


class Statement(object): pass


class Assign(Statement):
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

    def repr(self, indent): 
        var = self.variable.__repr__() if not getattr(self.variable,'repr', None) else self.variable.repr(indent+8)
        exp = self.expression.__repr__() if not getattr(self.expression,'repr',None) else self.expression.repr(indent+8)
        return 'Assign\n' + indent*' ' + var + indent*' ' + 'Value\n' + (indent+4)*' ' + exp


class Block(Statement):
    def __init__(self, statement_list, declarations=None):
        self.statement_list = statement_list
        self.declarations = declarations

    def repr(self, indent):
        s = 'Block Start\n'
        if self.declarations:
            s += indent*' ' + 'Using\n'
            for var_list in self.declarations:
                datatype = var_list[0]
                for var in var_list[1]:
                    s += (indent+4)*' ' + datatype + '\n' + (indent+8)*' ' + var.repr(indent+12)
            s += indent*' ' + 'In\n'

        for statement in self.statement_list:
            sta = statement.__repr__() if not getattr(statement,'repr',None) else statement.repr(indent+4)
            if sta != 'None':
                s += indent*' ' + sta
        return s + (indent-4)*' ' + 'Block End\n'


class Scan(Statement):
    def __init__(self, variable):
        self.variable = variable
        
    def repr(self, indent):
        var = self.variable.__repr__() if not getattr(self.variable,'repr',None) else self.variable.repr(indent+4)
        return 'Scan\n' + indent*' ' + var


class Print(Statement):
    def __init__(self, print_list):
        self.print_list = print_list

    def repr(self, indent):
        return_string = 'Print\n'
        for element in self.print_list:
            e = element.__repr__() if not getattr(element,'repr',None) else element.repr(indent+4)
            return_string += indent*' ' + e
        return return_string


class Println(Statement):
    def __init__(self, print_list):
        self.print_list = print_list

    def repr(self, indent):
        return_string = 'Println\n'
        for element in self.print_list:
            e = element.__repr__() if not getattr(element,'repr',None) else element.repr(indent+4)
            return_string +=  + indent*' ' + e
        return return_string


class If(Statement):
    def __init__(self, expression, statement1, statement2=None):
        self.expression = expression
        self.statement1 = statement1
        self.statement2 = statement2
    
    def repr(self, indent):
        exp = self.expression.__repr__() if not getattr(self.expression,'repr',None) else self.expression.repr(indent+8)
        sta_1 = self.statement1.__repr__() if not getattr(self.statement1,'repr',None) else self.statement1.repr(indent+8)
        s = 'If\n' + indent*' ' + 'Condition\n' + (indent+4)*' ' + exp + indent*' ' + 'Statement True\n' + (indent+4)*' ' + sta_1
        if self.statement2:
            sta_2 = self.statement2.__repr__() if not getattr(self.statement2,'repr',None) else self.statement2.repr(indent+8)
            return s + indent*' ' + 'Statement False\n' + (indent+4)*' ' + sta_2 + (indent-4)*' ' + 'End If\n'
        return s + (indent-4)*' ' + 'End If\n'


class For(Statement):
    def __init__(self, variable, order, expression, statement):
        self.variable = variable
        self.order = order
        self.expression = expression
        self.statement = statement

    def repr(self, indent):
        var = self.variable.__repr__() if not getattr(self.variable,'repr',None) else self.variable.repr(indent+4)
        exp = self.expression.__repr__() if not getattr(self.expression,'repr',None) else self.expression.repr(indent+8)
        sta = self.statement.__repr__() if not getattr(self.statement,'repr',None) else self.statement.repr(indent+8)
        return 'For\n' + indent*' ' + var + indent*' ' + 'Direction\n' + (indent+4)*' ' + self.order + '\n' + indent*' ' + 'In\n' + (indent+4)*' '  + exp + indent*' ' + 'Do\n' + (indent+4)*' ' + sta + (indent-4)*' ' + 'End For\n'


class Repeat(Statement):
    def __init__(self, statement1, expression, statement2):
        self.statement1 = statement1
        self.expression = expression
        self.statement2 = statement2
    
    def repr(self, indent):
        exp = self.expression.__repr__() if not getattr(self.expression,'repr',None) else self.expression.repr(indent+8)
        if self.statement1:
            sta_1 = self.statement1.__repr__() if not getattr(self.statement1,'repr',None) else self.statement1.repr(indent+4)
            s = 'Repeat\n' + indent*' ' + sta_1 + (indent-4)*' ' + 'While\n' + indent*' ' + 'Condition\n' + (indent+4)*' ' + exp
            if self.statement2:
                sta_2 = self.statement2.__repr__() if not getattr(self.statement2,'repr',None) else self.statement2.repr(indent+4)
                return s + (indent-4)*' ' + 'Do\n' + indent*' ' + sta_2 + (indent-4)*' ' + 'End Repeat\n'
            else:
                return s + (indent-4)*' ' + 'End Repeat\n'
        else:
            sta_2 = self.statement2.__repr__() if not getattr(self.statement2,'repr',None) else self.statement2.repr(indent+8)
            return 'While\n' + indent*' ' + 'Condition\n' + (indent+4)*' ' + exp + indent*' ' + 'Do\n' + (indent+4)*' ' +  sta_2 + '\n' + indent*' ' + 'End While\n'
        
    
class Expression(object): pass


class Variable(Expression):
    def __init__(self, name, var_type=None, value=None, lineno=None, column=None):
        self.name = name
        self.var_type = var_type
        self.value = value
        self.lineno = lineno
        self.column = column

    def repr(self, indent):
        if getattr(self.name,'repr',None):
            return str(self.name.repr(indent))
        else: 
            return 'Variable\n' + indent*' ' + str(self.name) + '\n'


class Int(Expression):
    def __init__(self, value):
        self.value = value
        
    def repr(self, indent):
        return 'Int\n' + indent*' ' + str(self.value) + '\n'
    
    def type(self): return 'int' 
    
    
class Set(Expression):
    def __init__(self, elements):
        self.elements = elements  
        
    def repr(self, indent):
        s = 'Set\n' + indent*' '
        for e in self.elements:
            s += str(e.__repr__()) if not getattr(e,'repr',None) else str(e.repr(indent+4)) + indent*' '
        return s[:len(s)-indent]
    
    def type(self): return 'set'
    
    
class Bool(Expression):
    def __init__(self, value):
        self.value = value

    def repr(self, indent):
        return 'Bool\n' + indent*' ' + self.value + '\n'
    
    def type(self): return 'bool'
    

class String(Expression):
    def __init__(self, value):
        self.value = value

    def repr(self, indent):
        return 'String\n' + indent*' ' + self.value + '\n'

    def type(self): return 'string'


class BinOp(Expression): 
    def __init__(self, operand1, operand2, lineno, column):
        self.operand1 = operand1
        self.operand2 = operand2
        self.lineno = lineno
        self.column = column
        self.init()

    def repr(self, indent):
        op1 = self.operand1.__repr__() if not getattr(self.operand1,'repr',None) else self.operand1.repr(indent+4)
        op2 = self.operand2.__repr__() if not getattr(self.operand2,'repr',None) else self.operand2.repr(indent+4)
        return self.__class__.__name__ + '\n' + indent*' ' + op1 + indent*' ' + op2

    def type(self):
        global static_checking_errors
        if self.operand1.type() == self.operand2.type(): return self.operand1.type()
        static_checking_errors += 'Error: Incompatible types for operator '+\
            self.__class__.__name__+": '"+self.operand1.type()+"' and '"+\
            self.operand2.type()+', in line '+str(self.lineno)+', column '+\
            str(self.column)+'.\n'
        return 'None'


class Plus(BinOp):
    def init(self):
        self.expected_type1 = 'int'
        self.expected_type2 = 'int'
        self.return_type = 'int'

class Minus(BinOp):
    def init(self):
        self.expected_type1 = 'int'
        self.expected_type2 = 'int'
        self.return_type = 'int'    

class Times(BinOp):
    def init(self):
        self.expected_type1 = 'int'
        self.expected_type2 = 'int'
        self.return_type = 'int'

class Div(BinOp):
    def init(self):
        self.expected_type1 = 'int'
        self.expected_type2 = 'int'
        self.return_type = 'int'
    
class Mod(BinOp):
    def init(self):
        self.expected_type1 = 'int'
        self.expected_type2 = 'int'
        self.return_type = 'int'
        
class PlusSet(BinOp):
    def init(self):
        self.expected_type1 = 'int'
        self.expected_type2 = 'set'
        self.return_type = 'set'

class MinusSet(BinOp):
    def init(self):
        self.expected_type1 = 'int'
        self.expected_type2 = 'set'
        self.return_type = 'set'
        
class TimesSet(BinOp):
    def init(self):
        self.expected_type1 = 'int'
        self.expected_type2 = 'set'
        self.return_type = 'set'
        
class DivSet(BinOp):
    def init(self):
        self.expected_type1 = 'int'
        self.expected_type2 = 'set'
        self.return_type = 'set'
        
class ModSet(BinOp):
    def init(self):
        self.expected_type1 = 'int'
        self.expected_type2 = 'set'
        self.return_type = 'set'
        
class LessThan(BinOp):
    def init(self):
        self.expected_type1 = 'int'
        self.expected_type2 = 'int'
        self.return_type = 'bool'
        
class LessThanEq(BinOp):
    def init(self):
        self.expected_type1 = 'int'
        self.expected_type2 = 'int'
        self.return_type = 'bool'
        
class GreaterThan(BinOp):
    def init(self):
        self.expected_type1 = 'int'
        self.expected_type2 = 'int'
        self.return_type = 'bool'
        
class GreaterThanEq(BinOp):
    def init(self):
        self.expected_type1 = 'int'
        self.expected_type2 = 'int'
        self.return_type = 'bool'
    
class Equals(BinOp):
    def init(self):
        pass    
    
class NotEquals(BinOp):
    def init(self):
        pass
        
class Union(BinOp):
    def init(self):
        self.expected_type1 = 'set'
        self.expected_type2 = 'set'
        self.return_type = 'set'

class Difference(BinOp):
    def init(self):
        self.expected_type1 = 'set'
        self.expected_type2 = 'set'
        self.return_type = 'set'
        
class Intersect(BinOp):
    def init(self):
        self.expected_type1 = 'set'
        self.expected_type2 = 'set'
        self.return_type = 'set'
        
class And(BinOp):
    def init(self):
        self.expected_type1 = 'bool'
        self.expected_type2 = 'bool'
        self.return_type = 'bool'
        
class Or(BinOp):
    def init(self):
        self.expected_type1 = 'bool'
        self.expected_type2 = 'bool'
        self.return_type = 'bool'
        
class Contains(BinOp):
    def init(self):
        self.expected_type1 = 'int'
        self.expected_type2 = 'set'
        self.return_type = 'bool'


class UnaryOp(Expression):
    def __init__(self, operand, lineno, column):
        self.operand = operand
        self.lineno = lineno
        self.column = column

    def repr(self, indent):
        op = self.operand.__repr__() if not getattr(self.operand,'repr',None) else self.operand.repr(indent+4)
        return self.__class__.__name__ + '\n' + indent*' ' + op

    def type(self):
        global static_checking_errors
        if self.operand.type() == self.expected_type: return self.return_type
        static_checking_errors += 'Error: Incompatible type for operator '+\
            self.__class__.__name__+": '"+self.operand.type()+"', in line "+str(self.lineno)+', column '+\
            str(self.column)+'.\n'
        return 'None'
    

class Uminus(UnaryOp):
    def init(self):
        self.expected_type = 'int'
        self.return_type = 'int'

class Not(UnaryOp):
    def init(self):
        self.expected_type = 'bool'
        self.return_type = 'bool'
        
class Len(UnaryOp):
    def init(self):
        self.expected_type = 'set'
        self.return_type = 'int'
        
class MaxSet(UnaryOp):
    def init(self):
        self.expected_type = 'set'
        self.return_type = 'int'
        
class MinSet(UnaryOp):
    def init(self):
        self.expected_type = 'set'
        self.return_type = 'int'