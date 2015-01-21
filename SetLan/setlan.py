import ply.lex as lex, sys

def find_column (inp, token):
    last_cr = inp.rfind('\n', 0, token.lexpos)
    if last_cr < 0: last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column


tokens = ('ID','Program','OpenCurly','CloseCurly','Using','Int','Colon','Scan',
          'OpenParen','CloseParen','Println','Print','In','Else','String',
          'LessThan','GreaterThan','LessThanEq','GreaterThanEq','Equals',
          'Comma','Assign','Plus','Comment','NotEquals','Contains','True',
          'False','Bool','Max','Min','Len','Sum','Res','Mul','Div','Mod',
          'Union','Difference','Intersect','Minus','Times','Divide','Modulus',
          'Number','For','Return','Def','Arrow','SemiColon',
          'Repeat','While','Set',)

t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
def t_Program(t):
    r'program'
    return t
t_OpenCurly = r'\{'
t_CloseCurly = r'\}'
def t_Using(t):
    r'using'
    return t
def t_Int(t):
    r'int'
    return t
t_Colon = r';'
def t_Scan(t):
    r'scan'
    return t
t_OpenParen = r'\('
t_CloseParen = r'\)'
def t_Println(t):
    r'println[; ]'
    return t
def t_Print(t):
    r'print '
    return t
def t_In(t):
    r'in '
    return t
def t_If(t):
    r'if '
    return t
def t_Else(t):
    r'else '
    return t
t_String = r'"[a-zA-Z_0-9]*"'

t_LessThan = r'<'
t_GreaterThan = r'>'
def t_LessThanEq(t):
    r'<='
    return t
def t_GreaterThanEq(t):
    r'>='
    return t
def t_Equals(t):
    r'=='
    return t
t_Comma = r','
t_Assign = r'='
t_Plus = r'\+'
t_Comment = r'\#'
t_NotEquals = r'/='
t_Contains = r'@'
def t_True(t):
    r'true[; ]'
    return t
def t_False(t):
    r'false'
    return t
def t_Bool(t):
    r'bool'
    return t
def t_Max(t):
    r'max'
    return t
def t_Min(t):
    r'min'
    return t
t_Len = r'\$\?'
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
t_Difference = r'\\'
def t_Intersect(t):
    r'><'
    return t
t_Minus = r'-'
t_Times = r'\*'
t_Divide = r'/'
t_Modulus = r'%'
def t_For(t):
    r'for '
    return t
def t_Return(t):
    r'return'
    return t
def t_Def(t):
    r'def '
    return t
def t_Arrow(t):
    r'->'
    return t
t_SemiColon = r':'
def t_Repeat(t):
    r'repeat '
    return t
def t_While(t):
    r'while '
    return t
def t_Set(t):
    r'set '
    return t
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters 
t_ignore = " \t"

def t_newline(t): 
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
        
def t_error(t): 
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    """need to modify this event to catch an invalid character
    ***********************************************************
    ***********************************************************
    """ 



def main():
    lexer = lex.lex()
    text = open(sys.argv[1],'r').read()
    lexer.input(text)
    for token in iter(lexer.token, None):
        print 'Token'+token.type+(': "'+token.value+'"' if token.type=='ID' else '')+'(Linea '+str(token.lineno)+', Columna '+str(find_column(text,token))+')'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
main()    # Uncomment to make executable 