import ply.lex as lex, sys

def find_column (inp, token):
    last_cr = inp.rfind('\n', 0, token.lexpos)
    if last_cr < 0: last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

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
    r'<*>'
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
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_String = r'".*?"'
#t_Comment = r'\#.*'
t_SemiColon = r':'
t_Difference = r'\\'
t_OpenCurly = r'\{'
t_CloseCurly = r'\}'
t_Colon = r';'
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


# Ignored characters 
t_ignore = " \t"
#t_ignore_comment = "#.*?"

def t_newline(t): 
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
        
        
s = ''
error_found = False
        
        
def t_error(t): 
    print("Illegal character '%s'" % t.value[0])
    error_found = True
    t.lexer.skip(1)

def main(arg):
    lexer = lex.lex()
    text = open(arg,'r').read()
    lexer.input(text)
    s = ''
    for token in iter(lexer.token, None):
        s += 'Token'+token.type+(': "'+token.value+'"' if token.type=='ID' else '')+'(Linea '+str(token.lineno)+', Columna '+str(find_column(text,token))+')\n'
    if not error_found:
        return s
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    main(sys.argv[1])