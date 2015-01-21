tokens = ('ID','PROGRAM','LCURLY','RCURLY','USING','INT','COLON','SCAN',
          'LPAREN','RPAREN','PRINTLN','PRINT','IN','IF','ELSE','DQUOTE',
          'LESSTHAN','GREATERTHAN','LESSTHANE','GREATERTHANE','EQUALS',
          'COMMA','ASSIGN','PLUS','HASHTAG','NEQUALS','CONTAINS','TRUE',
          'FALSE','BOOL','MAX','MIN','LEN','SUM','RES','MUL','DIV','MOD',
          'UNION','DIFFERENCE','INTERSECT','MINUS','TIMES','DIVIDE','MODULUS',
          'MAXINT','MININT','NUMBER','FOR','RETURN','DEF','ARROW','SEMICOLON',
          'REPEAT','WHILE','SET',) 

t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_PROGRAM = r'program'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_USING = r'using'
t_INT = r'int'
t_COLON = r';'
t_SCAN = r'scan'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PRINTLN = r'println'
t_IN = r'in'
t_IF = r'if'
t_ELSE = r'else'
t_DQUOTE = r'"'
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_LESSTHANE = r'<='
t_GREATERTHANE = r'>='
t_EQUALS = r'=='
t_COMMA = r','
t_ASSIGN = r'='
t_PLUS = r'\+'
t_HASHTAG = r'#'
t_NEQUALS = r'/='
t_CONTAINS = r'@'
t_TRUE = r'true'
t_FALSE = r'false'
t_BOOL = r'bool'
t_MAX = r'max'
t_MIN = r'min'
t_LEN = r'$?'
t_SUM = r'<+>'
t_RES = r'<->'
t_MUL = r'<*>'
t_DIV = r'</>'
t_MOD = r'<%>'
t_UNION = r'++'
t_DIFFERENCE = r'\\'
t_INTERSECT = r'><'
t_MINUS = r'-'
t_TIMES = r'*'
t_DIVIDE = r'/'
t_MODULUS = r'%'
t_MAXINT = r'max'
t_MININT = r'min'
t_FOR = r'for'
t_RETURN = r'return'
t_DEF = r'def'
t_ARROW = r'->'
t_SEMICOLON = r':'
t_REPEAT = r'repeat'
t_WHILE = r'while'
t_SET = r'set'



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