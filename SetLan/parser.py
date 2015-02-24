from lexer import *
import ply.yacc as yacc
from ast import *
from st import *

def p_program(p):
    "program : Program statement"
    p[0] = Program(p[2])


def p_assing(p):
    "statement : ID Assign expression"
    p[0] = Assign(Variable(p[1]), p[3])


def p_block(p):
    """statement : OpenCurly statement_list SemiColon CloseCurly
                 | OpenCurly Using new_scope declarations_list SemiColon scope_filled In statement_list CloseCurly
                 | """
    if len(p) == 5:
        p[0] = Block(p[2])
    elif len(p) == 10:
        global scopes_list, static_checking_log
        indent = (len(scopes_list)-1)*4 
        static_checking_log += indent*' ' + 'End Scope\n'
        scopes_list.pop()
        p[0] = Block(p[8],p[4])
    else:
        p[0] = None


def p_scope_filled(p):
    'scope_filled :'
    global scopes_list, static_checking_log
    indent = (len(scopes_list)-1)*4
    static_checking_log += indent*' ' + 'Scope\n'
    for v in scopes_list[len(scopes_list)-1].scope.values():
        static_checking_log += (indent+4)*' ' + 'Variable: ' + v.name + ' | Type: ' + \
                                v.var_type + ' | Value: ' + str(v.value) + '\n'


def p_new_scope(p):
    'new_scope :'
    global scopes_list
    scopes_list.append(SymbolTable())


def p_declarations_list(p):
    """declarations_list : type variable_list
                         | declarations_list SemiColon type variable_list"""
    global static_checking_errors, lexer
    if len(p) == 3:
        p[0] = [(p[1], p[2])]
        for var in p[2]:
            if scopes_list[len(scopes_list)-1].contains(var.name):
                static_checking_errors += 'Error: Redeclaration: variable \''+\
                var.name+'\', in line '+str(p.lineno(2))+', column '+str(p.lexpos(2))+'.\n'
            else:
                scopes_list[len(scopes_list)-1].insert(var)
    else:
        p[0] = p[1] + [(p[3], p[4])]
        for var in p[4]:
            if scopes_list[len(scopes_list)-1].contains(var.name):
                static_checking_errors += 'Error: Redeclaration: variable \''+\
                var.name+'\', in line '+str(p.lineno(2))+', column '+str(p.lexpos(2))+'.\n'
            else:
                scopes_list[len(scopes_list)-1].insert(var)


def p_variable_list(p):
    """variable_list : ID
                     | variable_list Comma variable_list"""
    var_value = False if actual_type == 'bool' else (0 if actual_type == 'int' else {})
    if len(p) == 2:
        p[0] = [Variable(p[1], actual_type, var_value, p.lineno, p.lexpos(1)-lexer.current_column)]
    else:
        #p[0] = p[1] + [Variable(p[3], actual_type, var_value, p.lineno, p.lexpos-lexer.current_column)]
        p[0] = p[1] + p[3]


def p_statement_list(p):
    """statement_list : statement
                      | statement_list SemiColon statement"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_type(p):
    """type : Int
            | Bool
            | Set"""
    p[0] = p[1]
    global actual_type
    actual_type = p[1]


def p_scan(p):
    "statement : Scan ID"
    p[0] = Scan(Variable(p[2]))


def p_print(p):
    """statement : Print expression_list
                 | Println expression_list"""
    if p[1] == 'print':
        p[0] = Print(p[2])
    else:
        p[0] = Println(p[2])


def p_expression_list(p):
    """expression_list : expression
                       | expression_list Comma expression"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_if(p):
    """statement : If OpenParen expression CloseParen statement
                 | If OpenParen expression CloseParen  statement Else statement"""
    if len(p) == 6:
        p[0] = If(p[3], p[5])
    else:
        p[0] = If(p[3], p[5], p[7])


def p_for(p):
    """statement : For new_scope ID scope_filled Min expression Do statement
                 | For new_scope ID scope_filled Max expression Do statement"""
    global lexer
    p[0] = For(Variable(p[3],'int',0,p.lineno,p.lexpos(3)-lexer.current_column), p[5], p[6], p[8])


def p_repeat(p):
    """statement : Repeat statement While OpenParen expression CloseParen Do statement
                 | Repeat statement While OpenParen expression CloseParen
                 | While OpenParen expression CloseParen Do statement"""
    if len(p) == 9:
        p[0] = Repeat(p[2], p[5], p[8])
    elif p[1] == 'repeat':
        p[0] = Repeat(p[2], p[5], None)
    elif p[1] == 'while':
        p[0] = Repeat(None, p[3], p[6])
        

precedence = (
    # bool x bool -> bool
    ("left", 'Or'),
    ("left", 'And'),
    ("right", 'Not'),
    # int x int -> bool
    ("nonassoc", 'LessThan', 'LessThanEq', 'GreaterThan', 'GreaterThanEq'),
    # int|set x int|set -> bool
    ("nonassoc", 'Equals', 'NotEquals'),
    # int x set -> bool
    ("nonassoc", 'Contains'),     
    # int
    ("left", 'Plus', 'Minus'),
    ("left", 'Times', 'Div', 'Mod'),
    # set x set -> set
    ("left", 'Union', 'Difference'),
    ("left", 'Intersect'),
    # int x set -> set
    ("left", 'PlusSet', 'MinusSet'),
    ("left", 'TimesSet', 'DivSet', 'ModSet'),          
    # set -> set    (unary set operators)
    ("right", 'MaxSet'),
    ("right", 'MinSet'),
    ("right", 'Len'),
    # Unary minus / negation
    ("right", 'Uminus'),
)


def p_int(p):
    "expression : Number"
    p[0] = Int(p[1])


def p_bool(p):
    """expression : True
                  | False"""
    p[0] = Bool(p[1].lower())


def p_string(p):
    "expression : String"
    p[0] = String(p[1])


def p_id(p):
    "expression : ID"
    global lexer
    p[0] = Variable(p[1], lineno = p.lineno, column = p.lexpos(1) - lexer.current_column)


def p_set_elements_list(p):
    """set_elements_list : Number
                         | arithmetic_op
                         | ID
                         | set_elements_list Comma Number
                         | set_elements_list Comma ID
                         | set_elements_list Comma arithmetic_op"""
    if len(p) == 2:
        try:
            if int(p[1]): p[0] = [Int(p[1])]
        except:
            p[0] = [Variable(p[1])]
    else:
        try:
            if int(p[3]):
                p[0] = p[1] + [Int(p[3])]
        except:
            if p[1] == None: p[1] = [Int('0')]
            p[0] = p[1] + [Variable(p[3])]


def p_set(p):
    """expression : OpenCurly set_elements_list CloseCurly
                  | OpenCurly CloseCurly"""
    p[0] = Set(p[2])


def p_parenthesis(p):
    """expression : OpenParen expression CloseParen"""
    p[0] = p[2]


def p_arithmetic_op(p):
    """arithmetic_op : expression Plus expression
                     | expression Minus expression
                     | expression Times expression
                     | expression Div expression
                     | expression Mod expression"""
    
    global lexer
    if p[2] == '+': p[0] = Plus(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
    elif p[2] == '-': p[0] = Minus(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
    elif p[2] == '*': p[0] = Times(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
    elif p[2] == '/': p[0] = Div(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
    elif p[2] == '%': p[0] = Mod(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)


def p_binop_(p):
    """expression : expression PlusSet expression
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
                  | expression Contains expression
                  | arithmetic_op"""

    if len(p) != 2:
        global lexer
        if p[2] == '<+>': p[0] = PlusSet(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
        elif p[2] == '<->': p[0] = MinusSet(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
        elif p[2] == '<*>': p[0] = TimesSet(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
        elif p[2] == '</>': p[0] = DivSet(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
        elif p[2] == '<%>': p[0] = ModSet(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
        elif p[2] == '<': p[0] = LessThan(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
        elif p[2] == '<=': p[0] = LessThanEq(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
        elif p[2] == '>': p[0] = GreaterThan(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
        elif p[2] == '>=': p[0] = GreaterThanEq(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
        elif p[2] == '==': p[0] = Equals(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
        elif p[2] == '/=': p[0] = NotEquals(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
        elif p[2] == '++': p[0] = Union(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
        elif p[2] == '\\': p[0] = Difference(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column) 
        elif p[2] == '><': p[0] = Intersect(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
        elif p[2] == 'and': p[0] = And(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
        elif p[2] == 'or': p[0] = Or(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
        elif p[2] == '@': p[0] = Contains(p[1], p[3], p.lineno, p.lexpos(2)-lexer.current_column)
    else:
        p[0] = p[1]


def p_unary_op(p):
    """expression : Minus expression %prec Uminus
                  | Not expression
                  | Len expression
                  | MaxSet expression
                  | MinSet expression"""
    if p[1] == '-': p[0] = Uminus(p[2], p.lineno, p.lexpos(1)-lexer.current_column)
    elif p[1] == 'not': p[0] = Not(p[2], p.lineno, p.lexpos(1)-lexer.current_column)
    elif p[1] == '$?': p[0] = Len(p[2], p.lineno, p.lexpos(1)-lexer.current_column)
    elif p[1] == '>?': p[0] = MaxSet(p[2], p.lineno, p.lexpos(1)-lexer.current_column)
    elif p[1] == '<?': p[0] = MinSet(p[2], p.lineno, p.lexpos(1)-lexer.current_column)


def p_error(p):
    global parsing_errors, lexer
    parsing_errors += 'Error: Unexpected \''+str(p.value)+'\' in line '+str(p.lineno)+', column '+str(p.lexpos - lexer.current_column)+'.\n'


parsing_errors = ''
static_checking_errors = ''
static_checking_log = ''
scopes_list = []
actual_type = None


def mainParser(arg):
    global parsing_errors, lexer
    lexer_return = mainLexer(arg)
    if(lexer_return.count('Error:') != 0):
        return lexer_return
    lexer = lex.lex()
    lexer.current_column = -1
    lexer.input(open(arg,'r').read())
    parsing_errors = ''
    parser = yacc.yacc()
    ast = parser.parse(open(arg,'r').read())
    if parsing_errors != '': return parsing_errors
    else: return ast.repr()


def mainStaticChecker(arg):
    global parsing_errors, lexer, scopes_list, actual_type, static_checking_log
    lexer_return = mainLexer(arg)
    if(lexer_return.count('Error:') != 0):
        return lexer_return
    lexer = lex.lex()
    lexer.current_column = -1
    lexer.input(open(arg,'r').read())
    parsing_errors = ''
    parser = yacc.yacc()
    parser.parse(open(arg,'r').read())
    if parsing_errors != '': return parsing_errors
    if static_checking_errors != '': return static_checking_errors
    return static_checking_log


if __name__ == '__main__':
    print(mainParser(sys.argv[1]))




