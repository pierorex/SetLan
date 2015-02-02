from lexer import *
from ast import *

def p_program(p):
    "program : Program statement"
    p[0] = Program(p[2])


def p_statement_assing(p):
    "statement : ID ASSIGN expression"
    p[0] = Assign(Variable(p[1]), p[3])


def p_statement_block(p):
    """statement : LCurly statement_list RCurly
                 | LCurly declare_list statement_list RCurly"""
    if len(p) == 4:
        p[0] = Block(p[2])
    else:
        p[0] = Block(p[4])


def p_statement_declare_list(p):
    """declare_list : using data_type declare_comma_list in
                    | data_type declara_comma_list in
                    | declare_list Semicolon declare_comma_list"""
    if len(p) == 4:
        p[0] = [(p[1], p[3])]
    else:
        p[0] = p[1] + [(p[3], p[5])]


def p_statement_declare_comma_list(p):
    """declare_comma_list : ID
                          | declare_comma_list Comma ID"""
    if len(p) == 2:
        p[0] = [Variable(p[1])]
    else:
        p[0] = p[1] + [Variable(p[3])]


# Multiple statements in a block statement have a separation token, the ';'
def p_statement_statement_list(p):
    """statement_list : statement
                      | statement_list Semicolon statement"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_data_type(p):
    """data_type : Int
                 | Bool
                 | Set"""
    p[0] = p[1]

###############################     IN/OUT      ###############################

def p_statement_print(p):
    """statement : Print comma_list
                 | Println comma_list"""
    if p[1] == 'Print':
        p[0] = Print(p[2])
    else:
        if len(p) == 3:
            p[0] = Print(p[2] + [String('"\\n"')])
        else:
            p[0] = Print([String('"\\n"')])


# To generate the list of elements for a 'print' or a 'println'
def p_statement_comma_list(p):
    """comma_list : expression
                  | comma_list Comma expression"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

############################     CONDITIONAL      #############################

def p_statement_if(p):
    """statement : If expression statement
                 | If expression statement Else statement"""
    if len(p) == 5:
        p[0] = If(p[2], p[4])
    else:
        p[0] = If(p[2], p[4], p[6])


###############################     LOOP      #################################


# The for statement, automatically declares an 'int' variable in the scope of
# the for, this variable has a value of every value in the range specified
def p_statement_for(p):
    "statement : For ID Min SetExpression Do statement"
    p[0] = For(Variable(p[2]), p[4], p[6])


# The while statement, while some condition holds, keep doing a statement
def p_statement_repeat(p):
    "statement : Repeat expression while condition DO statement"
    p[0] = Repeat(p[2], p[4])

###############################################################################
#############################     EXPRESSIONS     #############################
###############################################################################


# Precedence defined for expressions
precedence = (
    # bools
    ("left", 'OR'),
    ("left", 'AND'),
    ("right", 'NOT'),
    # comparissons
    ("nonassoc", 'Equals'),
    ("nonassoc", 'Less', 'LessThanEq', 'Grater', 'GreaterThanEq'),
    # sets
    ()
    # ints
    ("left", 'PLUS', 'MINUS'),
    ("left", 'TIMES', 'DIVIDE', 'MODULO'),
    ("right", 'UMINUS'),
    # set
)

##############################     LITERALS     ###############################


# A number is a valid expression
def p_exp_int_literal(p):
    "expression : NUMBER"
    p[0] = Int(p[1])


# A boolean is a valid expression
def p_exp_bool_literal(p):
    """expression : True
                  | False"""
    p[0] = Bool(p[1].lower())


# A string is a valid expression
def p_exp_string_literal(p):
    "expression : String"
    p[0] = String(p[1])


# An ID is a variable expression, since an ID is an int, bool or set
def p_expression_id(p):
    "expression : ID"
    p[0] = Variable(p[1])


def p_int_list(p):
    """int_list : Int
                | int_list Comma Int"""

def p_expression_set(p):
    """expression : LCurly int_list RCurly"""


# An expression between parenthesis is still an expression
def p_expression_group(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]

#############################     OPERATORS     ###############################


# Binary operators defined for int
def p_exp_int_binary(p):
    """expression : expression PLUS   expression
                  | expression MINUS  expression
                  | expression TIMES  expression
                  | expression DIVIDE expression
                  | expression MODULO expression"""
    operator = {
        '+': 'PLUS',
        '-': 'MINUS',
        '*': 'TIMES',
        '/': 'DIVIDE',
        '%': 'MODULO'
    }[p[2]]
    p[0] = Binary(operator, p[1], p[3])


# Unary minus, defined for int
def p_exp_int_unary(p):
    "expression : MINUS expression %prec UMINUS"
    p[0] = Unary('MINUS', p[2])


# Binary operators defined for range
def p_exp_range_binary(p):
    """expression : expression INTERSECTION expression"""
    operator = 'INTERSECTION'
    p[0] = Binary(operator, p[1], p[3])


# Considered these functions as unary operators for range
def p_exp_int_range_unary(p):
    """expression : RTOI   LPAREN expression RPAREN
                  | LENGTH LPAREN expression RPAREN
                  | TOP    LPAREN expression RPAREN
                  | BOTTOM LPAREN expression RPAREN"""
    p[0] = Unary(p[1].upper(), p[3])


# Binary operators defined for bool
def p_exp_bool_binary(p):
    """expression : expression OR      expression
                  | expression AND     expression"""
    operator = {
        'or': 'OR',
        'and': 'AND',
    }[p[2]]
    p[0] = Binary(operator, p[1], p[3])


# Unary not, defined for bool
def p_exp_bool_unary(p):
    "expression : NOT expression"
    if isinstance(p[2], Bool):
        expr = eval(p[2].value.title())
        expr = str(not expr).upper()
        p[0] = Bool(expr)
    else:
        p[0] = Unary(p[1].upper(), p[2])


# Binary operators to compare
def p_exp_bool_compare(p):
    """expression : expression LESS    expression
                  | expression LESSEQ  expression
                  | expression GREAT   expression
                  | expression GREATEQ expression
                  | expression EQUAL   expression
                  | expression UNEQUAL expression"""
    operator = {
        '<': 'LESS',
        '<=': 'LESSEQ',
        '>': 'GREAT',
        '>=': 'GREATEQ',
        '==': 'EQUAL',
        '/=': 'UNEQUAL'
    }[p[2]]
    p[0] = Binary(operator, p[1], p[3])
    
    
def mainParser():
    pass
    
if __name__ == '__main__':
    print(mainParser(sys.argv[1]))    