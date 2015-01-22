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
          'Len','PlusSet','MinusSet','TimesSet','DivSet','ModSet','Union',
          'Difference','Intersect','Minus','Times','Div','Mod','Number','Arrow',
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
def t_PlusSet(t):
    r'<\+>'
    return t
def t_MinusSet(t):
    r'<->'
    return t
def t_TimesSet(t):
    r'<\*>'
    return t
def t_DivSet(t):
    r'</>'
    return t
def t_ModSet(t):
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
t_Div = r'/'
t_Mod = r'%'


def t_newline(t): 
    r'\n+'
    global current_column
    t.lexer.lineno += t.value.count("\n")
    t.lexer.current_column = t.lexer.lexpos - 1

# Ignored characters 
t_ignore = " \t"
t_ignore_COMMENT = r'\#.*'
    

# Global variables to return information
string = ''
errors = ''
        
def t_error(t):
    global errors
    errors += 'Error: Se encontro un caracter inesperado "'+t.value[0]+'" en la Linea '+str(t.lexer.lineno)+', Columna '+str(t.lexer.lexpos - t.lexer.current_column)+'.\n'
    t.lexer.skip(1)

def main(arg):
    global errors, string
    errors, string, = '', ''
    lexer = lex.lex()
    lexer.current_column = -1
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
            
        string += 'Token'+token.type+(': '+str(token.value) if token.type=='ID' or token.type=='String' or token.type=='Number' else '')+' (Linea '+str(token.lineno)+', Columna '+str(token.lexpos - lexer.current_column)+')\n'
    print found_tokens
    
    return string if len(errors) == 0 else errors
    
    
if __name__ == '__main__':
    print(main(sys.argv[1]))
    