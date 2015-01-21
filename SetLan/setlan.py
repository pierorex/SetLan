tokens = ('ID','PROGRAM','LCURLY','RCURLY','USING','INT','COLON','SCAN',
          'LPAREN','RPAREN','PRINTLN','PRINT','IN','IF','ELSE','DQUOTE',
          'LESSTHAN','GREATERTHAN','LESSTHANE','GREATERTHANE','EQUALS',
          'COMMA','ASSIGN','PLUS','HASHTAG','NEQUALS','CONTAINS','TRUE',
          'FALSE','BOOL','MAX','MIN','LEN','SUM','RES','MUL','DIV','MOD',
          'UNION','DIFFERENCE','INTERSECT','MINUS','TIMES','DIVIDE','MODULUS',
          'NUMBER','FOR','RETURN','DEF','ARROW','SEMICOLON',
          'REPEAT','WHILE','SET',) 

t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
def t_PROGRAM(t): 
    r'program'
    return t
t_LCURLY = r'\{'
t_RCURLY = r'\}'
def t_USING(t):
    r'using'
    return t
def t_INT(t):
    r'int'
    return t
t_COLON = r';'
def t_SCAN(t):
    r'scan'
    return t
t_LPAREN = r'\('
t_RPAREN = r'\)'
def t_PRINTLN(t):
    r'println'
    return t
def t_IN(t):
    r'in'
    return t
def t_IF(t):
    r'if'
    return t
def t_ELSE(t):
    r'else'
    return t
t_DQUOTE = r'"'
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
def t_LESSTHANE(t):
    r'<='
    return t
def t_GREATERTHANE(t):
    r'>='
    return t
def t_EQUALS(t):
    r'=='
    return t
t_COMMA = r','
t_ASSIGN = r'='
t_PLUS = r'\+'
t_HASHTAG = r'\#'
t_NEQUALS = r'/='
t_CONTAINS = r'@'
def t_TRUE(t):
    r'true'
    return t
def t_FALSE(t):
    r'false'
    return t
def t_BOOL(t):
    r'bool'
    return t
def t_MAX(t):
    r'max'
    return t
def t_MIN(t):
    r'min'
    return t
t_LEN = r'\$\?'
def t_SUM(t):
    r'<\+>'
    return t
def t_RES(t):
    r'<->'
    return t
def t_MUL(t):
    r'<*>'
    return t
def t_DIV(t):
    r'</>'
    return t
def t_MOD(t):
    r'<%>'
    return t
def t_UNION(t):
    r'\+\+'
    return t
t_DIFFERENCE = r'\\'
def t_INTERSECT(t):
    r'><'
    return t
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULUS = r'%'
def t_FOR(t):
    r'for'
    return t
def t_RETURN(t):
    r'return'
    return t
def t_DEF(t):
    r'def'
    return t
def t_ARROW(t):
    r'->'
    return t
t_SEMICOLON = r':'
def t_REPEAT(t):
    r'repeat'
    return t
def t_WHILE(t):
    r'while'
    return t
def t_SET(t):
    r'set'
    return t
t_NUMBER = r'\d+'

# Ignored characters 
t_ignore = " \t"

def t_newline(t): 
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
        
def t_error(t): 
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    """need to intercept this event to catch the invalid character
    ***********************************************************
    ***********************************************************
    """ 
    
# Build the lexer
import ply.lex as lex
lex.lex()