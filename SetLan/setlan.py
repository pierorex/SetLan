import ply.lex as lex, sys

reserved = {
    'program' : 'Program',
    'using' : 'Using',
    'int' : 'Int',
    'scan' : 'Scan',
    'print' : 'Print',
    'println' : 'Println',
    'in' : 'In',
    'if' : 'If',
    'else' : 'Else',
    'true' : 'True',
    'false' : 'False',
    'bool' : 'Bool',
    'max' : 'Max',
    'min' : 'Min',
    'for' : 'For',
    'return' : 'Return',
    'def' : 'Def',
    'repeat' : 'Repeat',
    'while' : 'While',
    'set' : 'Set'
    }

tokens = ['ID','OpenCurly','CloseCurly','Colon','OpenParen','CloseParen',
          'String','LessThan','GreaterThan','LessThanEq','GreaterThanEq',
          'Equals','Comma','Assign','Plus','Comment','NotEquals','Contains',
          'Len','Sum','Res','Mul','Div','Mod','Union','Difference',
          'Intersect','Minus','Times','Divide','Modulus','Number','Arrow',
          'SemiColon'] + list(reserved.values())

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t
def t_LessThanEq(t):
    r'<='
    return t
def t_GreaterThanEq(t):
    r'>='
    return t
def t_Equals(t):
    r'=='
    return t
def t_Sum(t):
    r'<\+>'
    return t
def t_Res(t):
    r'<->'
    return t
def t_Mul(t):
    r'<\*>'
    return t
def t_Div(t):
    r'</>'
    return t
def t_Mod(t):
    r'<%>'
    return t
def t_Union(t):
    r'\+\+'
    return t
def t_Intersect(t):
    r'><'
    return t
def t_Arrow(t):
    r'->'
    return t
def t_Number(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_String = r'".*?"'
t_Colon = r':'
t_Difference = r'\\'
t_OpenCurly = r'\{'
t_CloseCurly = r'\}'
t_SemiColon = r';'
t_OpenParen = r'\('
t_CloseParen = r'\)'
t_LessThan = r'<'
t_GreaterThan = r'>'
t_Comma = r','
t_Assign = r'='
t_Plus = r'\+'
t_NotEquals = r'/='
t_Contains = r'@'
t_Len = r'\$\?'
t_Minus = r'-'
t_Times = r'\*'
t_Divide = r'/'
t_Modulus = r'%'

current_column = -1

def t_newline(t): 
    r'\n+'
    global current_column
    t.lexer.lineno += t.value.count("\n")
    current_column = t.lexer.lexpos - 1

# Ignored characters 
t_ignore = " \t"
t_ignore_COMMENT = r'\#.*'

def find_column (inp, token):
    last_cr = inp.rfind('\n', 0, token.lexpos)
    if last_cr < 0: last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

    
string = ''
errors = ''
text = ''

        
def t_error(t):
    global errors, text, current_column
    errors += 'Error: Se encontro un caracter inesperado "'+t.value[0]+'" en la Linea '+str(t.lexer.lineno)+', Columna '+str(t.lexer.lexpos - current_column)+'.\n'
    t.lexer.skip(1)

def main(arg):
    global errors, text, string, current_column
    errors, text, string, current_column = '', '', '', -1
    lexer = lex.lex()
    text = open(arg,'r').read()
    lexer.input(text)
    string = ''
    found_tokens = {
        'reserved': [],
        'numbers': [],
        'operators': [],
        'identifiers': []
    }
    for token in iter(lexer.token, None):
        if token.type == 'ID': found_tokens['identifiers'].append(token)
        elif token.type == 'Number': found_tokens['numbers'].append(token)
        elif token.type in reserved.values(): found_tokens['reserved'].append(token)
        else: found_tokens['operators'].append(token)
        string += 'Token'+token.type+(': "'+token.value+'"' if token.type=='ID' else '')+'(Linea '+str(token.lineno)+', Columna '+str(token.lexpos - current_column)+')\n'
    print found_tokens
    return string if len(errors) == 0 else errors
    
    
    
if __name__ == '__main__':
    main(sys.argv[1])
    