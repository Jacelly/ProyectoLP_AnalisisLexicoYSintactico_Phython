#Ejercicio 1
nota = int(input("Ingrese nota: "))
if nota >0 and nota<5:
    print("Insuficiente")
elif nota<8 :
    print("Suficiente")
elif nota<9 :
    print("Notable")
elif nota<11 :
    print("Sobresaliente")
else:
    print("Nota invalida")

#Ejercicio 2
entrada = 5.50
print('Tipo de cliente')
print('1. niños de 0 - 5')
print('2. niños de 6 - 12')
print('3. adultos')
print('4. 3era edad')
tipo = input('Elija tipo de cliente: ')
if tipo=='1':
    print("Los niños menores a 5 no pagan")
elif tipo=='2':
    print('Costo de la entrada es:',entrada*.5)
elif tipo=='3':
    print('Costo de la entrada es:',entrada)
elif tipo=='4':
    print('Costo de la entrada es:',entrada*.6)
else:
    print('Tipo de cliente invalido')

#Ejercicio 3
print("Calcular jornal diario de empleados")
d = 40
n = 100
domingo = input("Es domingo? s/n")
diurnas = int(input("Cuantas horas trabajo en turno diurno? "))
nocturnas = int(input("Cuantas horas trabajo en turno nocturno? "))
if domingo=="s":
    print("Trabajo",diurnas,"horas diurnas y",nocturnas,"horas nocturnas")
    print("Su pago es:",(diurnas*(d+100))+(nocturnas*(n+200)))
elif domingo=="n":
    print("Trabajo",diurnas,"horas diurnas y",nocturnas,"horas nocturnas")
    print("Su pago es:",(diurnas*d)+(nocturnas*n))
else:
    print("Criterios invalidos")

#Ejercicio 4
print("Claculo de horas extras")
valorxHora = float(input("ingrese el valor por hora a pagar: "))
horas = int(input("Ingrese las horas que trabajo a la semana: "))
extras = 0
if horas<= 40:
    print("No tiene horas extras, su sueldo es:", horas*valorxHora)
else:
    extras= horas-40
    if extras<=8:
        print("Tiene",extras,"horas extras, su sueldo es:",(horas*valorxHora)+(extras*(valorxHora*2)))
    else:
        print("Tiene", extras, "horas extras, su sueldo es:", (horas * valorxHora) + (8 * (valorxHora * 2))+((extras-8) * (valorxHora * 2)))

