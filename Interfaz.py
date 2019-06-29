import tkinter
from tkinter import *
from tkinter import ttk
from SINTACTICO_PYTHON import *
#from funciones_extra import *
from LEXICO_PYTHON import *
#from sintactico import errors_list as e_l

from ejerciciosPropuestos import *
raiz = Tk()
n = 0


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
        btnNext.place(x=550,y=380)
    else:
        retroalimentacion.set("CODIGO ERRONEO\nEl código podría ser:\n"+ejerciciosResueltos[n])
        btnNext.place_forget()



btnExaminer = ttk.Button(raiz, text='EXAMINAR', command=ejecutar)
btnExaminer.place(x=550,y=350)


def siguiente():
    retroalimentacion.set("RETROALIMENTACION")
    ingresoCodigo.delete('1.0', 'end+1c')
    analisisLexico.set("ANALISIS LEXICO")
    analisisSintactico.set("ANALISIS SINTACTICO")
    global n
    n+=1
    if n < len(ejercicios):
        problema.set(ejercicios[n])
        btnNext.place_forget()
    else:
        problema.set("FELICIDADES\nHas acabado todos los niveles.")
        btnExaminer.place_forget()
        btnNext.place_forget()

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
lexico.config(font=("Arial",8))
sintactico.place(x=710,y=280,height=240,width=400)
sintactico.config(font=("Arial",10))

retroalimentacion = StringVar()
retroalimentacion.set("RETROALIMENTACION")
correccion = tkinter.Label(raiz, textvariable=retroalimentacion)
correccion.config(font=("Arial",8))

correccion.place(x=400,y=530,height=150,width=400)
btnNext = ttk.Button(raiz, text='SIGUIENTE', command=siguiente)
btnNext.place(x=550,y=380)
btnNext.place_forget()


raiz.configure(bg = 'lightblue')
raiz.title('PROYECTO LENGUAJES')

raiz.mainloop()