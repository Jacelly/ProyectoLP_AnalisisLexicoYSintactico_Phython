import tkinter
from tkinter import *
from tkinter import ttk
from SINTACTICO_PYTHON import *
#from funciones_extra import *
from LEXICO_PYTHON import *
#from sintactico import errors_list as e_l

from ejerciciosPropuestos import *
raiz = Tk()
contador = 0


raiz.geometry("1200x750")
titulo = "PROBLEMA"
etiquetaTitulo = tkinter.Label(raiz, text=titulo)
etiquetaTitulo.config(fg="blue", font=("Comic Sans MS",18,"bold "))
etiquetaTitulo.pack(padx=10, pady=5)
problema = StringVar()
problema.set(ejercicios[0])
etiquetaProblema = tkinter.Label(raiz, textvariable =problema,wraplength=1000)
etiquetaProblema.config( font=("Comic Sans MS",10,"bold "))
etiquetaProblema.pack()
ingresoCodigo = tkinter.Text(raiz)

ingresoCodigo.config(width=130, height=5)
ingresoCodigo.place(x=80,y=160)



def ejecutar():
    ingreso = obtenerCodigo()
    
    resultado, isCorrect= analisisSintacticof(ingreso)
    analisisLexico.set(resultado)
    analisisSintactico.set(str(isCorrect))
    if isCorrect:
        retroalimentacion.set("CODIGO CORRECTO")
    else:
        retroalimentacion.set("CODIGO ERRONEO")



ttk.Button(raiz, text='EXAMINAR', command=ejecutar).place(x=550,y=350)

n =0

def siguiente():
    retroalimentacion.set("")
    ingresoCodigo.delete('1.0', 'end+1c')
    analisisLexico.set("ANALISIS LEXICO")
    analisisSintactico.set("ANALISIS SINTACTICO")
    global n
    n+=1
    if n < len(ejercicios):
        problema.set(ejercicios[n])
    else:
        problema.set("SIGUIENTE NIVEL")
def obtenerCodigo():
    codigo = ingresoCodigo.get('1.0', 'end+1c')
    print(codigo)
    codigo = (codigo.strip()).replace("  ","")
    codigo = codigo.replace("\n"," ")
    print(codigo)
    return codigo


analisisLexico = StringVar()
analisisLexico.set("ANALISIS LEXICO")
lexico = tkinter.Label(raiz, textvariable=analisisLexico ,wraplength=1000)

analisisSintactico = StringVar()
analisisSintactico.set("ANALISIS SINTACTICO")
sintactico = tkinter.Label(raiz, textvariable=analisisSintactico ,wraplength=1000)

lexico.place(x=90,y=280,height=240,width=400)
lexico.config(font=("Arial",7))
sintactico.place(x=710,y=280,height=240,width=400)
sintactico.config(font=("Arial",7))

retroalimentacion = StringVar()
retroalimentacion.set("retroalimentacion")
correccion = tkinter.Label(raiz, textvariable=retroalimentacion)
correccion.config(font=("Arial",7))

correccion.place(x=400,y=530,height=150,width=400)
ttk.Button(raiz, text='SIGUIENTE', command=siguiente).place(x=550,y=380)


raiz.configure(bg = 'lightblue')
raiz.title('PROYECTO LENGUAJES')

raiz.mainloop()