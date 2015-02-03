from lexer import *
import ply.yacc as yacc
from ast import *

def p_program(p):
    "program : Program statement"
    p[0] = Program(p[2])


def p_statement_assing(p):
    "statement : ID Assign expression"
    p[0] = Assign(Variable(p[1]), p[3])


def p_statement_block(p):
    """statement : OpenCurly statement_list CloseCurly
                 | OpenCurly Using variable_list In statement_list CloseCurly"""
    if len(p) == 4:
        p[0] = Block(p[2])
    else:
        p[0] = Block(p[4])


def p_statement_variable_list(p):
    """variable_list : data_type variable_comma_list
                     | variable_list SemiColon data_type variable_comma_list"""
    if len(p) == 3:
        p[0] = [(p[1], p[2])]
    else:
        p[0] = p[1] + [(p[2], p[3])]


def p_statement_variable_comma_list(p):
    """variable_comma_list : ID
                           | variable_comma_list Comma ID"""
    if len(p) == 2:
        p[0] = [Variable(p[1])]
    else:
        p[0] = p[1] + [Variable(p[3])]


def p_statement_statement_list(p):
    """statement_list : statement
                      | statement_list SemiColon statement"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_data_type(p):
    """data_type : Int
                 | Bool
                 | Set"""
    p[0] = p[1]


def p_statement_scan(p):
    "statement : Scan ID"
    p[0] = Scan(Variable(p[2]))


def p_statement_print(p):
    """statement : Print comma_list
                 | Println comma_list"""
    if p[1] == 'Print':
        p[0] = Print(p[2])
    elif len(p) == 3:
        p[0] = Print(p[2] + [String('"\\n"')])
    else:
        p[0] = Print([String('"\\n"')])


def p_statement_comma_list(p):
    """comma_list : expression
                  | comma_list Comma expression"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_statement_if(p):
    """statement : If expression statement
                 | If expression statement Else statement"""
    if len(p) == 4:
        p[0] = If(p[2], p[3])
    else:
        p[0] = If(p[2], p[3], p[5])


def p_statement_for(p):
    """statement : For ID Min expression Do statement
                 | For ID Max expression Do statement"""
    p[0] = For(Variable(p[2]), p[3], p[4], p[6])


def p_statement_repeat(p):
    """statement : Repeat statement While expression Do statement
                 | Repeat statement While expression
                 | While expression Do statement"""
    if len(p) == 7:
        p[0] = Repeat(p[2], p[4], p[6])
    elif p[1] == 'Repeat':
        p[0] = Repeat(p[2], p[4])
    elif p[1] == 'While':
        p[0] = While(p[2], p[4])
        

precedence = (
    # set -> set    (unary set operators)
    ("right", 'MaxSet'),
    ("right", 'MinSet'),
    ("right", 'Len'),
    # int x set -> set
    ("left", 'PlusSet', 'MinusSet'),
    ("left", 'TimesSet', 'DivSet', 'ModSet'),
    # int x set -> bool
    ("right", 'Contains'),
    # set x set -> set
    ("left", 'Union', 'Difference'),
    ("left", 'Intersect'),
    # int
    ("left", 'Plus', 'Minus'),
    ("left", 'Times', 'Div', 'Mod'),
    ("right", 'Uminus'),
    # int x int -> bool
    ("nonassoc", 'LessThan', 'LessThanEq', 'GreaterThan', 'GreaterThanEq'),
    # int|set x int|set -> bool
    ("nonassoc", 'Equals', 'NotEquals'),
    # bool x bool -> bool
    ("left", 'Or'),
    ("left", 'And'),
    ("right", 'Not'),
)


def p_exp_int_literal(p):
    "expression : Number"
    p[0] = Int(p[1])


def p_exp_bool_literal(p):
    """expression : True
                  | False"""
    p[0] = Bool(p[1].lower())


def p_exp_string_literal(p):
    "expression : String"
    p[0] = String(p[1])


def p_expression_id(p):
    "expression : ID"
    p[0] = Variable(p[1])


def p_number_list(p):
    """number_list : Number
                | number_list Comma Number"""

def p_expression_set(p):
    """expression : OpenCurly number_list CloseCurly"""


def p_expression_parenthesis(p):
    """expression : OpenParen expression CloseParen"""
    p[0] = p[2]


def p_binop(p):
    """expression : expression Plus expression
                  | expression Minus expression
                  | expression Times expression
                  | expression Div expression
                  | expression Mod expression
                  | expression PlusSet expression
                  | expression MinusSet expression
                  | expression TimesSet expression
                  | expression DivSet expression
                  | expression ModSet expression
                  | expression LessThan expression
                  | expression LessThanEq expression
                  | expression GreaterThan expression
                  | expression GreaterThanEq expression
                  | expression Equals expression
                  | expression NotEquals expression
                  | expression Union expression
                  | expression Difference expression
                  | expression Intersect expression
                  | expression And expression
                  | expression Or expression
                  | expression Contains expression"""
    
    if p[2] == '+': p[0] = Plus(p[1], p[2])
    elif p[2] == '-': p[0] = Minus(p[1], p[2])
    elif p[2] == '*': p[0] = Times(p[1], p[2])
    elif p[2] == '/': p[0] = Div(p[1], p[2])
    elif p[2] == '%': p[0] = Mod(p[1], p[2])
    elif p[2] == '<+>': p[0] = PlusSet(p[1], p[2])
    elif p[2] == '<->': p[0] = MinusSet(p[1], p[2])
    elif p[2] == '<*>': p[0] = TimesSet(p[1], p[2])
    elif p[2] == '</>': p[0] = DivSet(p[1], p[2])
    elif p[2] == '<%>': p[0] = ModSet(p[1], p[2])
    elif p[2] == '<': p[0] = LessThan(p[1], p[2])
    elif p[2] == '<=': p[0] = LessThanEq(p[1], p[2])
    elif p[2] == '>': p[0] = GreaterThan(p[1], p[2])
    elif p[2] == '>=': p[0] = GreaterThanEq(p[1], p[2])
    elif p[2] == '==': p[0] = Equals(p[1], p[2])
    elif p[2] == '\=': p[0] = NotEquals(p[1], p[2])
    elif p[2] == '++': p[0] = Union(p[1], p[2])
    elif p[2] == '\\': p[0] = Difference(p[1], p[2]) 
    elif p[2] == '><': p[0] = Intersect(p[1], p[2])
    elif p[2] == 'and': p[0] = And(p[1], p[2])
    elif p[2] == 'or': p[0] = Or(p[1], p[2])
    elif p[2] == '@': p[0] = Contains(p[1], p[2])


def p_unary_op(p):
    """expression : Minus expression %prec Uminus
                  | Not expression
                  | Len expression
                  | MaxSet expression
                  | MinSet expression"""
    if p[1] == '-': p[0] = Uminus(p[2])
    elif p[1] == 'not': p[0] = Not(p[2])
    elif p[1] == '$?': p[0] = Len(p[2])
    elif p[1] == '>?': p[0] = MaxSet(p[2])
    elif p[1] == '<?': p[0] = MinSet(p[2])
    
    
        
def mainParser(arg):
    parser = yacc.yacc(start='program')
    
    
    
if __name__ == '__main__':
    print(mainParser(sys.argv[1]))
    