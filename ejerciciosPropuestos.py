ejercicios=["1.	Escribe un programa que pida la nota de un estudiante y diga que si es mayor a 6 está aprobado y menor a 6 está reprobado",
            "2. Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.",
            "3.	Escribir un programa en Python que determine el precio a pagar en una entrada del cine, el valor de los tickets es 5,50, sabiendo que:"
            "\n•Los niños de 0-5 no pagan y los niños de 6 a 12 pagan la mitad.",
            "4. Escriba un programa que determine si un número es par o impar.",
            "5.	Los empleados de una fábrica trabajan en turno diurno. Se desea calcular el jornal diario de acuerdo con los siguientes puntos: "
            "\n•La tarifa de horas diurnas es de $40. "
            "\n•Caso de ser Domingo, la tarifa se incrementará en $100 en el turno diurno",
            "6.	Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa, sabiendo que cuando las horas de trabajo exceden de 40, el resto se consideran horas extras y que estas se pagan al doble de una hora normal.",
            "7. EScriba una función que dado un radio calcule el area de un circulo, dado su radio",
            "8. Escriba una función que dado un dividendo y un divisor devuelva su división pero si el divisor es cero retorne 'No se puede'"]


ejerciciosResueltos = ["nota = int(input('Ingrese nota: '))\nif nota >= 6:\nprint('Aprobado')\nelse:\nprint('Reprobado')",
                       "edad = int(input('¿Cuál es tu edad?'))\nif edad < 18:\nprint ('Eres menor de edad.')\nelse:print('Eres mayor de edad.')",
                       "entrada = 5.50\nprint('Tipo de cliente')\nprint('1. niños de 0 - 5')\nprint('2. niños de 6 - 12')\ntipo = input('Elija tipo de cliente: ')\nif tipo == '1':\nprint('Los niños menores a 5 no pagan')\nelse:\nprint('Costo de la entrada es:', entrada * .5)",
                       "num = int(input('Ingrese un numero: '))\nif num%2 == 0:\nprint('Es numero par.')\nelse:print('Es numero impar.')",
                       "print('Calcular jornal diario de empleados')\nd = 40\ndomingo = input('Es domingo? s/n')\ndiurnas = int(input('Cuantas horas trabajo en turno diurno?'))\nif domingo == 's':\nprint('Trabajo', diurnas, 'horas diurnas')\nprint('Su pago es:', (diurnas * (d + 100)))\nelse:\nprint('Trabajo', diurnas, 'horas diurnas')\nprint('Su pago es:', (diurnas * d))",
                       "horas = int(input('Cuantas horas ha trabajado: '))\nif horas == 40:\nprint('No tiene pago de horas extras')\nelse:\nhorasExtras = horas-40\nprint('Ha trabajado ',horasExtras,' de horas extras')\nprint('Su pago es de: ',horasExtras*2)",
                       "def area(radio):\narea = radio*3.14159\nprint('El área del circulo es: ',area)",
                       "def division(num1,num2):\ndivision = num1/num2\nif num2 == 0:\nreturn 'No se puede'\nelse:\nreturn division"]