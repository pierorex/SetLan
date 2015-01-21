tokens = ('ID','PROGRAM','LCURLY','RCURLY','USING','INT','COLON','SCAN',
          'LPAREN','RPAREN','PRINTLN','PRINT','IN','IF','ELSE','DQUOTE',
          'LESSTHAN','GREATERTHAN','LESSTHANE','GREATERTHANE','EQUALS',
          'COMMA','ASSIGN','PLUS','HASHATAG','NEQUALS','CONTAINS','TRUE',
          'FALSE','BOOL','MAX','MIN','LEN','SUM','RES','MUL','DIV','MOD',
          'UNION','DIFFERENCE','INTERSECT','MINUS','TIMES','DIVIDE','MODULUS',
          'MAXINT','MININT','NUMBER','FOR','RETURN','DEF','ARROW','SEMICOLON',
          'REPEAT','WHILE','SET','') 
# Tokens 
t_PLUS = r'\+' 
t_MINUS = r'-' 
t_TIMES = r'\*' 
t_DIVIDE = r'/' 
t_EQUALS = r'=' 
t_LPAREN = r'\(' 
t_RPAREN = r'\)' 
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*' 

def t_NUMBER(t): 
    r'\d+' 
    try: 
        t.value = int(t.value) 
    except ValueError: 
        print("Integer value too large %d", t.value) 
        t.value = 0 
    return t 
        
# Ignored characters 
t_ignore = " \t" 

def t_newline(t): 
    r'\n+' 
    t.lexer.lineno += t.value.count("\n") 
    
def t_error(t): 
    print("Illegal character '%s'" % t.value[0]) 
    t.lexer.skip(1) 
    
# Build the lexer
import ply.lex as lex
lex.lex()