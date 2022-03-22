from lexer import lexer, tokens
from ply.yacc import yacc

def p_programa(p):
    '''
    programa : PROGRAM ID SEMICOLON programa1
    '''

def p_programa1(p):
    '''
    programa1 : vars bloque 
              | bloque
    '''

def p_vars(p):
    '''
    vars : VAR vars1
    '''

def p_vars1(p):
    '''
    vars1 : vars2 COLON tipo SEMICOLON 
          | vars2 COLON tipo SEMICOLON vars1
    '''

def p_vars2(p):
    '''
    vars2 : ID
	      | ID COMMA vars2
    '''

def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
    '''

def p_bloque(p):
    '''
    bloque : LCURLY bloque1 RCURLY
	       | LCURLY RCURLY
    '''

def p_bloque1(p):
    '''
    bloque1 : estatuto bloque1
	        | estatuto
    '''

def p_estatuto(p):
    '''
    estatuto : asignacion
	         | condicion
	         | escritura
    '''

def p_asignacion(p):
    '''
    asignacion : ID EQUALS expresion SEMICOLON
    '''

def p_condicion(p):
    '''
    condicion : IF LPAREN expresion RPAREN bloque condicion2
    '''

def p_condicion2(p):
    '''
    condicion2 : SEMICOLON
	           | ELSE bloque SEMICOLON
    '''

def p_escritura(p):
    '''
    escritura : PRINT LPAREN escritura1 RPAREN SEMICOLON
    '''

def p_escritura1(p):
    '''
    escritura1 : escritura2
		       | escritura2 COMMA escritura1
    '''

def p_escritura2(p):
    '''
    escritura2 : expresion
		       | STRING
    '''

def p_expresion(p):
    '''
    expresion : exp 
	          | exp expresion1 exp
    '''

def p_expresion1(p):
    '''
    expresion1 : MORE
		       | LESS
		       | NOT
    '''

def p_exp(p):
    '''
    exp : termino 
        | termino exp1 exp
    '''

def p_exp1(p):
    '''
    exp1 : PLUS
	     | MINUS
    '''

def p_termino(p):
    '''
    termino : factor
	        | factor termino1 factor
    '''

def p_termino1(p):
    '''
    termino1 : TIMES
	         | DIVIDE
    '''

def p_factor(p):
    '''
    factor : LPAREN expresion RPAREN
	       | PLUS var_cte
	       | MINUS var_cte
	       | var_cte
    '''

def p_var_cte(p):
    '''
    var_cte : ID
	        | NUMBER
	        | DECIMAL
    '''

def p_error(p):
    print(f'Syntax error at {p.value!r} at line {p.lineno}')
    exit()

parser = yacc(debug=True)
