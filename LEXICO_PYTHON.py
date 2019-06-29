import ply.lex as lex

#Palabras reservadas
palabrasReservadas={
    'if':'IF',  #*
    'else':'ELSE',  #*
    'elif':'ELIF',  #*
    'def':'DEF',  #OK
    'print':'PRINT',  #OK
    'True':'TRUE',  #OK
    'False':'FALSE',  #OK
    'not':'NOT',  #OK
    'and':'AND',  #OK
    'or':'OR',  #OK
    'upper':'UPPER',  #*
    'lower':'LOWER',  #*
    'in':'IN',  #OK
    'return':'RETURN',  #OK
    'is':'IS',  #OK
    'index':'INDEX',  #*
    'count':'COUNT',  #*
    'len':'LEN',  #OK
    'append':'APPEND',#OK
    'remove':'REMOVE',#*
    'min':'MIN',  #*
    'max':'MAX',  #*
    'extend':'EXTEND',#*
    'sort':'SORT',#*
    'reverse':'REVERSE',#*
    'pop':'POP',#*
    'split':'SPLIT',#*
    'join':'JOIN',#*
    'input':'INPUT', #OK
    'int' : 'INT'   #OK
}
# Lista de tokens
tokens = [
   'VARIABLE','FLOTANTE','NUMERO','CADENACOMILLADOBLE','CADENACOMILLASIMPLE','DIFERENTE','PUNTO','MAS','MENOS','POR','DIVIDIR',
   'APARENT','CPARENT', 'CORIZQ','CORDER','LLAIZQ','LLADER', 'ASIGNACION','MAYOR', 'MENOR',
   'MAYORIGUAL', 'MENORIGUAL','DOSPUNTOS', 'MODULO', 'DOBLECOMILLA', 'SIMPLECOMILLA',
   'DOBLEIGUAL','COMA', 'POTENCIA'
]+ list(palabrasReservadas.values())
#PALABRAS RESERVADAS

def t_VARIABLE(t):  #OK
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palabrasReservadas.get(t.value, 'VARIABLE')
    return t

def t_FLOTANTE(t):  #OK
    r'\d+\.\d+'
    return t

def t_NUMERO(t):    #OK
    r'\d+'
    t.value = int(t.value)
    return t
def t_CADENACOMILLADOBLE(t): #OK
   r'\"[\w|\ ]+[\w*|\d*|\+*|\ *|\,*|\-*|\:*|\.*|\ *]*\"'
   return t
def t_CADENACOMILLASIMPLE(t): #OK
   r'\'[\w|\ ]+[\w*|\d*|\+*|\ *|\,*|\-*|\:*|\.*|\ *]*\''
   return t

#TOKENS
t_DIFERENTE = r'\!=' #OK
t_PUNTO = r'\.'  #Ok
t_MAS    = r'\+'    #OK
t_MENOS   = r'-'    #OK
t_POR   = r'\*' #OK
t_DIVIDIR  = r'/'  #OK
t_APARENT  = r'\('  #OK
t_CPARENT  = r'\)'  #OK
t_CORIZQ = r'\['    #OK
t_CORDER = r'\]'    #OK
t_LLAIZQ = r'\{'    #OK
t_LLADER = r'\}'    #OK
t_ASIGNACION = r'\='    #OK
t_MAYOR = r'\>' #OK
t_MENOR = r'\<' #OK
t_MAYORIGUAL = r'\>=' #OK
t_MENORIGUAL = r'\<=' #OK
t_DOSPUNTOS = r'\:'  #OK
t_MODULO = r'\%'    #OK
t_DOBLECOMILLA = r'\"'  #OK
t_SIMPLECOMILLA = r'\'' #OK
t_DOBLEIGUAL = r'\=\='  #OK
t_COMA = r'\,'  #OK
t_POTENCIA = r'\*\*' #OK

#REGLAS PROPIAS DE LEX

# Define una regla para que podamos rastrear números de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Una cadena que contiene caracteres ignorados (espacios y tabs)
t_ignore = ' \t'

#Regla de manejo de errores
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# CONSTRUIR EL  LEXER
lexer = lex.lex()


# PRUEBAS
data = '''
 a = {3 + 4 * 10
   + -20 *2}_GX
 .8>=9'Y=5*9'
 s and b == 5 else
 endy
 is 5 in,8
 5.23
 min(l)
 '''
data1 = '''
'Elija tipo de cliente: gg'
"Elija tipo de cliente: gg"

 '''

#LE DAMOS AL LEXER ALGUNA ENTRADA PARA PROBAR
#lexer.input(data)
lexer.input(data1)
# TOKENIZAR
#while True:
 #   tok = lexer.token()
  #  if not tok:
   #     break  #NO MAS ENTRADA
    #print(tok) #Formato: LexRoken(type, value, lineno, lexpos)
