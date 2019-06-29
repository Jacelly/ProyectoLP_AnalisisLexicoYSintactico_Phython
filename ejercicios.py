# Ejercicio 1
nota = int(input("Ingrese nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Reprobado")

#Ejercicio2
edad = int(input("¿Cuál es tu edad? "))
if edad < 18:
    print ("Eres menor de edad.")
else:
    print("Eres mayor de edad.")

# Ejercicio 3
entrada = 5.50
print('Tipo de cliente')
print('1. niños de 0 - 5')
print('2. niños de 6 - 12')
tipo = input('Elija tipo de cliente: ')
if tipo == '1':
    print("Los niños menores a 5 no pagan")
else:
    print('Costo de la entrada es:', entrada * .5)

# Ejercicio 4
num = int(input("Ingrese un numero: "))
if num%2 == 0:
    print("Es numero par.")
else:
    print("Es numero impar.")

# Ejercicio 5
print("Calcular jornal diario de empleados")
d = 40
domingo = input("Es domingo? s/n")
diurnas = int(input("Cuantas horas trabajo en turno diurno? "))
if domingo == "s":
    print("Trabajo", diurnas, "horas diurnas")
    print("Su pago es:", (diurnas * (d + 100)))
else:
    print("Trabajo", diurnas, "horas diurnas")
    print("Su pago es:", (diurnas * d))

# Ejercicio 6
horas = int(input("Cuantas horas ha trabajado: "))
if horas == 40:
    print("No tiene pago de horas extras")
else:
    horasExtras = horas-40
    print("Ha trabajado ",horasExtras," de horas extras")
    print("Su pago es de: ",horasExtras*2)

#Ejercicio 7
def area(radio):
    area = radio*3.14159
    print("El área del circulo es: ",area)

#Ejercicio 8
def division(num1,num2):
    division = num1/num2
    if num2 == 0:
        return "No se puede"
    else:
        return division

#Ejercicio 9
if 19%2 == 0:
    print("No es numero primo")
else:
    print("Si es numero primo")

#Ejercicio 10
def append(list,element):
    list.append(element)
    return list