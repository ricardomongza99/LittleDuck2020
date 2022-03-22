from sly import Parser
from lexer import DuckLexer

class DuckParser(Parser):
    
    tokens = DuckLexer.tokens
    debugfile = 'parser.out'

    # Grammar rules and actions
    @_('PROGRAM ID SEMICOLON programa1')
    def programa(self, p):
        pass

    @_('vars bloque', 'bloque')
    def programa1(self, p):
        pass

    @_('VAR vars1')
    def vars(self, p):
        pass

    @_('vars2 COLON tipo SEMICOLON', 'vars2 COLON tipo SEMICOLON vars1')
    def vars1(self, p):
        pass

    @_('ID', 'ID COMMA vars2')
    def vars2(self, p):
        pass

    @_('INT', 'FLOAT')
    def tipo(self, p):
        pass

    @_('LCURLY bloque1 RCURLY', 'LCURLY RCURLY')
    def bloque(self, p):
        pass

    @_('estatuto bloque1', 'estatuto')
    def bloque1(self, p):
        pass

    @_('asignacion', 'condicion', 'escritura')
    def estatuto(self, p):
        pass

    @_('ID EQUALS expresion SEMICOLON')
    def asignacion(self, p):
        pass

    @_('IF LPAREN expresion RPAREN bloque condicion2')
    def condicion(self, p):
        pass

    @_('SEMICOLON', 'ELSE bloque SEMICOLON')
    def condicion2(self, p):
        pass

    @_('PRINT LPAREN escritura1 RPAREN SEMICOLON')
    def escritura(self, p):
        pass

    @_('escritura2', 'escritura2 COMMA escritura1')
    def escritura1(self, p):
        pass

    @_('expresion', 'STRING')
    def escritura2(self, p):
        pass

    @_('exp', 'exp expresion1 exp')
    def expresion(self, p):
        pass

    @_('MORE', 'LESS', 'NOT')
    def expresion1(self, p):
        pass

    @_('termino', 'termino exp1 exp')
    def exp(self, p):
        pass

    @_('PLUS', 'MINUS')
    def exp1(self, p):
        pass

    @_('factor', 'factor termino1 factor')
    def termino(self, p):
        pass

    @_('TIMES', 'DIVIDE')
    def termino1(self, p):
        pass

    @_('LPAREN expresion RPAREN', 'PLUS var_cte', 'MINUS var_cte', 'var_cte')
    def factor(self, p):
        pass

    @_('ID', 'NUMBER', 'DECIMAL')
    def var_cte(self, p):
        pass