from ply.lex import lex

# FILENAME = 'program2.duck'

# with open(FILENAME, 'r') as file:
#     data = file.read().replace('\n', '')


reserved = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
    'if': 'IF',
    'else': 'ELSE',
    'print': 'PRINT'
}

# Token names
tokens = [
        'ID', 
        'NUMBER', 
        'DECIMAL',
        'STRING', 
        'COMMA',
        'SEMICOLON',
        'COLON',
        'LCURLY',
        'RCURLY',
        'LPAREN',
        'RPAREN',
        'MORE',
        'LESS',
        'NOT',
        'EQUALS',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE'] + list(reserved.values())

# Token regex rules
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'
t_LCURLY = r'{'
t_RCURLY = r'}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MORE = r'>'
t_LESS = r'<'
t_NOT = r'<>'
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'

# Token regex rules with action code
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_DECIMAL(t):
    r'\d+.\d+'
    t.value = float(t.value)    
    return t

def t_STRING(t):
    # TODO: add symbols
    r'\"[a-zA-Z0-9_!\s]*\"'
    t.value = t.value[1:-1]
    return t

# Rule to track line numbers
def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Ignored characters
t_ignore = ' \t'

# Error handler for illegal characters
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)


lexer = lex()

    # lexer.input(data)

    # # Tokenize
    # while True:
    #     tok = lexer.token()
    #     if not tok:
    #         break   # no more input
    #     print(tok)
