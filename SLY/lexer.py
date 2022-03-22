from ast import If
from ctypes.wintypes import FLOAT
from sly import Lexer

class DuckLexer(Lexer):

    tokens = {'PROGRAM', 'VAR', 'INT', 'FLOAT', 'IF', 'ELSE', 'PRINT',
            'ID', 'NUMBER', 'DECIMAL', 'STRING', 'COMMA', 'SEMICOLON', 'COLON',
            'LCURLY', 'RCURLY', 'LPAREN', 'RPAREN', 'MORE', 'LESS', 'NOT', 'EQUALS',
            'PLUS', 'MINUS', 'TIMES', 'DIVIDE'}
    
    ignore = ' \t'

    # Token regex rules
    PROGRAM   = r'program '
    VAR       = r'var '
    INT       = r'int'
    FLOAT     = r'float'
    IF        = r'if'
    ELSE      = r'else'
    PRINT     = r'print'
    COMMA     = r','
    SEMICOLON = r';'
    COLON     = r':'
    LCURLY    = r'{'
    RCURLY    = r'}'
    LPAREN    = r'\('
    RPAREN    = r'\)'
    MORE      = r'>'
    LESS      = r'<'
    NOT       = r'<>'
    EQUALS    = r'='
    PLUS      = r'\+'
    MINUS     = r'-'
    TIMES     = r'\*'
    DIVIDE    = r'\/'
    ID        = r'[a-zA-Z_][a-zA-Z_0-9]*'

    # Token regex rules with action code
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'\d+.\d+')
    def DECIMAL(self, t):
        t.value = float(t.value)
        return t

    @_(r'\"[a-zA-Z0-9_!\s]*\"')
    def STRING(self, t):
        t.value = t.value[1:-1]
        return t

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
    
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1