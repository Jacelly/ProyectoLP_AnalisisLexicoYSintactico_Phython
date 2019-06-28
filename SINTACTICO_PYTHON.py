import ply.yacc as yacc
import ply.lex as lex
import LEXICO_PYTHON

tokens = LEXICO_PYTHON.tokens

# resultado del analisis
resultado_gramatica = []
errors_list=[]
#LAS PRECEDENCIAS(PROCEDURE) LAS UTILIZAMOS PARA ESPECIFICAR LAS PREFERENCIAS DE ORDEN EN LAS OPERACIONES
# Y CUALQUIER OTRO AMBITO QUE POSEA UNA PREFERENCIA DE ORDEN
precedence = (
    ('right','ASIGNACION'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIR'),
    ('right', 'UMINUS'),
)

#DECLARAR UNA VARIABLE Y ASIGNAR CUALQUIER TIPO DE EXPRESION(NUMERO,FLOTANTE,BOOLEANO,STRING,ETC)
def p_declaracion_asignar(t):#ok
    '''
    declaracion : VARIABLE ASIGNACION expresion
                    | VARIABLE ASIGNACION declaracion
    '''
    print("prueba1")
    t[0] = (t[1],t[3])

def p_declaracion_expr(t):#ok
    '''
    declaracion : expresion
                | VARIABLE
                | FLOTANTE
                | expr_funcion
                | lista
                | expr_def_funcion
                | expr_return
                | if
                | expr_print
                | append
                | len
                | input
                | in
                | is
                | join
                | int
                | upper
                | lower
    '''
    print("prueba2")
    t[0] = t[1]

#BOOLEANOS
def p_boolean(t):#ok
    '''
    expresion : TRUE
            | FALSE
    '''
    print("prueba3")
    t[0] = t[1]

#EXPRESIONES ARITMETICAS
def p_expresion_operaciones(t):#ok
    '''
    expresion  :   expresion MAS expresion
                |   expresion MENOS expresion
                |   expresion POR expresion
                |   expresion DIVIDIR expresion
                |   expresion POTENCIA expresion
                |   expresion MODULO expresion
    '''
    print("prueba4")
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '%':
        t[0] = t[1] % t[3]
    elif t[2] == '**':
        i = t[3]
        t[0] = t[1]
        while i > 1:
            t[0] *= t[1]
            i -= 1

# PRECEDENCIA DE OPERACIONES ARITMETICAS EN LAS CUALES SE RESPETAN LAS OPERACIONES  Y EL SIGNO NEGTIVO
def p_expresion_uminus(t):#ok
    'expresion : MENOS expresion %prec UMINUS'
    print("prueba5")
    t[0] = -t[2]

#EXPRESIONES DE AGRUPACION
def p_expresion_grupo(t):#ok
    '''
    expresion  : APARENT expresion CPARENT
                | LLAIZQ expresion LLADER
                | CORIZQ expresion CORDER
    '''
    print("prueba6")
    t[0] = t[2]

# EXPRESIONES COMPARACION
def p_expresion_logicas(t):#ok
    '''
    expresion   :  expresion MENOR expresion
                |  expresion MAYOR expresion
                |  expresion MENORIGUAL expresion
                |   expresion MAYORIGUAL expresion
                |   expresion DOBLEIGUAL expresion
                |   expresion DIFERENTE expresion
                |  APARENT expresion CPARENT MENOR APARENT expresion CPARENT
                |  APARENT expresion CPARENT MAYOR APARENT expresion CPARENT
                |  APARENT expresion CPARENT MENORIGUAL APARENT expresion CPARENT
                |  APARENT  expresion CPARENT MAYORIGUAL APARENT expresion CPARENT
                |  APARENT  expresion CPARENT DOBLEIGUAL APARENT expresion CPARENT
                |  APARENT  expresion CPARENT DIFERENTE APARENT expresion CPARENT
    '''
    print("bbbbbbbbb")
    if t[2] == "<":
        t[0] = t[1] < t[3]
    elif t[2] == ">":
        t[0] = t[1] > t[3]
    elif t[2] == "<=":
        t[0] = t[1] <= t[3]
    elif t[2] == ">=":
        t[0] = t[1] >= t[3]
    elif t[2] == "==":
        t[0] = t[1] == t[3]
    elif t[2] == "!=":
        t[0] = t[1] != t[3]
    elif t[4] == "<":
        t[0] = t[2] < t[6]
    elif t[4] == ">":
        t[0] = t[2] > t[6]
    elif t[4] == "<=":
        t[0] = t[2] <= t[6]
    elif t[4] == ">=":
        t[0] = t[2] >= t[6]
    elif t[4] == "==":
        t[0] = t[2] == t[6]
    elif t[4] == "!=":
        t[0] = t[2] != t[4]

# EXPRESIONES LOGICAS
def p_expresion_booleana(t):
    '''
    expresion   : declaracion AND declaracion
                |   declaracion OR declaracion
                |  NOT declaracion
                |  APARENT declaracion AND declaracion CPARENT
                |  APARENT declaracion OR declaracion CPARENT
                |  APARENT NOT declaracion CPARENT

    '''
    print("prueba7")
    print(t[2])
    print(t[1])
    if t[2] == "and":
        t[0] = t[1] and t[3]
    elif t[2] == "or":
        t[0] = t[1] or t[3]
    elif t[1] == "not":
        t[0] = not t[2]
    elif t[3] == "and":
        t[0] = t[2] and t[4]
    elif t[3] == "or":
        t[0] = t[2] or t[4]
    elif t[2] == "not":
        t[0] = not t[3]
    else:
        t[0] = False

    #NUMERO
def p_expresion_numero(t): #OK
    'expresion : NUMERO'
    print("prueba8")
    t[0] = t[1]

#CADENA
def p_expresion_cadena(t):#OK
    """expresion : CADENACOMILLADOBLE
               | CADENACOMILLASIMPLE
    """
    print("prueba9")
    t[0]=t[1]

#NOMBRE VARIABLE
#def p_expresion_nombre_Variable(t):
 #   'expresion : VARIABLE'
  #  print("prueba10")
   # t[0] = t[1]

#EXPRESIONES PARA DEFINIR FUNCIONES
#RECUERDA: MAYUSCULAS TOKENS Y PALABRAS RESERVADAS, Y minusculas EXPRESIONES POR DEFINIR SU BNF
def p_expr_funcion(t):# OK
    'expr_funcion : VARIABLE APARENT params CPARENT'
    print("prueba11")
    t[0]=(t[1],t[3])
def p_variable(t): #OK
    """
    variable : VARIABLE
                | NUMERO
                | FLOTANTE
                | expr_funcion
                | expresion
                | lista
                """
    print("prueba13")
    t[0]=t[1]
def p_params(t): #OK
    """
    params : variable
            | params COMA params
    """
    print("prueba12")
    if(len(t)==2):
        t[0]=t[1]
    elif(len(t)==4):
        t[0]=(t[1],t[3])
#def p_expr_float(t):
#    """expr_float : FLOTANTE"""
#    print("prueba14")
#    t[0]=t[1]

def p_lista(t): #OK
    """
    lista : VARIABLE ASIGNACION CORIZQ CORDER
          | VARIABLE ASIGNACION CORIZQ NUMERO CORDER
          | VARIABLE ASIGNACION CORIZQ VARIABLE CORDER
    """
    print("prueba15")
    t[0]=('LISTA')

def p_expr_def_funcion(t): #OK
    """expr_def_funcion : DEF expr_funcion DOSPUNTOS"""
    print("prueba16")
    t[0]=('FUNCION')

#EXPRESIONES PARA IMPLEMENTAR CODIGO INTERNO
#def p_linea_codigo(t):
 #   """
  #  linea_codigo : expresion
   #              | expr_funcion
    #             | declaracion
     #            | expr_return
   # """
    #print("prueba17")
    #t[0]=t[1]

#def p_expr_asign(t):
 #   """expr_asign : VARIABLE ASIGNACION variable"""
  #  print("prueba18")
   # t[0]=t[3]

def p_expr_return(t):   #OK
    """expr_return : RETURN variable"""
    print("prueba19")
    t[0]=t[2]

def p_codigo_interno(t):
    """
    codigo_interno :	declaracion
                    | codigo_interno declaracion
    """
    print("prueba20")
    t[0]=t[1]

#EXPRESION PARA EL  DEFINIR  SENTENCIAS CONDICIONALES
def p_if(t):
    """
    if : IF APARENT expresion CPARENT DOSPUNTOS codigo_interno
       | IF expresion DOSPUNTOS codigo_interno
       | IF expresion DOSPUNTOS
       | IF APARENT expresion CPARENT DOSPUNTOS codigo_interno ELSE DOSPUNTOS codigo_interno
       | IF expresion DOSPUNTOS codigo_interno ELSE DOSPUNTOS codigo_interno
       | IF APARENT  expresion CPARENT DOSPUNTOS codigo_interno ELIF APARENT expresion CPARENT DOSPUNTOS codigo_interno ELSE DOSPUNTOS codigo_interno
       | IF expresion DOSPUNTOS codigo_interno ELIF expresion DOSPUNTOS codigo_interno ELSE DOSPUNTOS codigo_interno
       | IF APARENT expresion CPARENT DOSPUNTOS codigo_interno ELIF APARENT expresion CPARENT DOSPUNTOS codigo_interno
       | IF expresion DOSPUNTOS codigo_interno ELIF expresion DOSPUNTOS codigo_interno
       | IF expresion DOSPUNTOS codigo_interno ELIF expresion DOSPUNTOS codigo_interno ELIF expresion DOSPUNTOS codigo_interno ELIF expresion DOSPUNTOS codigo_interno ELSE DOSPUNTOS codigo_interno
    """
    print("prueba21")
    if(len(t)==7):
        t[0] = (t[1], t[3], t[6])
    elif(len(t)==4):
        t[0] = (t[1], t[2])
    elif(len(t)==5):
        t[0] = (t[1], t[2], t[4])
    elif(len(t)==10):
        t[0] = (t[1], t[3], t[6],t[7],t[9])
    elif(len(t)==8):
        t[0] = (t[1], t[2], t[4],t[5],t[7])
    elif (len(t) == 16):
        t[0] = (t[1], t[3], t[6],t[7],t[9],t[12],t[13],t[15])
    elif (len(t) == 12):
        t[0] = (t[1], t[2], t[4], t[5], t[6], t[8], t[9], t[11])
    elif (len(t) == 13):
        t[0] = (t[1], t[3], t[6], t[7], t[9],t[12])
    elif (len(t) == 9 and t[5]=='elif'):
        t[0] = (t[1], t[2], t[4], t[5],t[6], t[8])

#EXPRESION PARA PRINT
def p_expr_print(t): #OK
    ''' expr_print : PRINT APARENT VARIABLE CPARENT
                   | PRINT  APARENT  expresion CPARENT
                   | PRINT APARENT expresion MAS VARIABLE CPARENT
                   | PRINT APARENT expresion MAS NUMERO CPARENT
                   | PRINT APARENT expresion MAS FLOTANTE CPARENT
                   | PRINT APARENT expresion COMA expr_funcion CPARENT
                   | PRINT APARENT expresion COMA NUMERO CPARENT
                   | PRINT APARENT expresion COMA FLOTANTE CPARENT
                   | PRINT APARENT expresion COMA VARIABLE CPARENT
                   | PRINT APARENT expresion COMA expresion CPARENT
    '''
    print("prueba22")
    if (len(t) == 5):
        t[0] = t[3]
    elif (len(t) == 7):
        t[0] = (t[3], t[5])

def p_expr_append(t): #OK
    '''
    append : VARIABLE PUNTO APPEND APARENT VARIABLE CPARENT
            | VARIABLE PUNTO APPEND APARENT NUMERO CPARENT
            | VARIABLE PUNTO APPEND APARENT FLOTANTE CPARENT
    '''
    print("prueba23")
    t[0] = ('APPEND')

def p_expr_in(t):
    '''
    in : IN
    '''
    print("prueba26")
    t[0] = t[1]

def p_expr_len(t): #OK
    '''
    len : LEN APARENT VARIABLE CPARENT
    '''
    print("prueba27")
    t[0] = len(t[3])

#MUESTRA EL ERROR SINTACTICO EN CASO DE HABERLO
def p_input(t): #OK
    '''
    input : INPUT APARENT CADENACOMILLADOBLE CPARENT
          | INPUT APARENT CADENACOMILLASIMPLE CPARENT
    '''
    t[0]=('INPUT')
    print("prueba28")
def p_in(t): #OK
    '''
    in : VARIABLE in declaracion
         |  NUMERO in declaracion
         | FLOTANTE in declaracion
         | expresion in declaracion
    '''
    print("prueba30")
    t[0]=('IN')
def p_is(t): #OK
    '''
    is : VARIABLE IS NUMERO
         | VARIABLE  IS FLOTANTE
         | VARIABLE  IS declaracion
    '''
    print("prueba31")
    t[0]=('IS')
def p_join(t):
    '''
    join : SIMPLECOMILLA VARIABLE SIMPLECOMILLA PUNTO JOIN APARENT VARIABLE CPARENT
         | SIMPLECOMILLA VARIABLE SIMPLECOMILLA PUNTO JOIN APARENT CADENACOMILLASIMPLE CPARENT
    '''
    print("prueba29")
    t[0]=('JOIN')
def p_int(t): #OK
    '''
    int : INT APARENT expresion  CPARENT
        | INT APARENT input  CPARENT
    '''
    t[0]=t[1]

def p_expr_upper(t): #OK
    '''
    upper : VARIABLE PUNTO UPPER APARENT CPARENT
    '''
    print("prueba24")
    t[0] = t[1].upper()

def p_expr_lower(t): #OK
    '''
    lower : VARIABLE PUNTO LOWER APARENT CPARENT
    '''
    print("prueba25")
    t[0] = t[1].lower()

def p_error(t):
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format( str(t.type),str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)

# INTANCIAMOS EL ANALIZADOR SINTACTICO
parser = yacc.yacc()

#FUNCION DE NALIZADOR LEXICO Y SINTACTICO
def analisisLexicof(texto):
    lex.input(texto)
    cadena = ""
    # TOKENIZAR
    while True:
        tok = lex.token()
        if not tok:
            break  # NO MAS ENTRADA
        print(tok)  # Formato: LexRoken(type, value, lineno, lexpos)
        cadena += str(tok)
        cadena += "\n"
    print('CADENA VÁLIDA (LÉXICO)')
    return cadena

def analisisSintacticof(texto):
    cadena = analisisLexicof(texto)
    resultado = parser.parse(texto)
    if resultado:
        print(resultado)
        return cadena, True
    else:
        return cadena,False





