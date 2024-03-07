#tabla de multiplicar
import os
numero = int(input('Ingrese un número entero positivo->'))
if numero < 0:
    print('Debes ingresar un número positivo')
else: 
    multiplicador =1
    os.system('cls')
    print('Esta es la tabla de multiplicar del:' , numero)
while multiplicador <= 10:

    resultado = numero * multiplicador
    print(numero,'x' ,multiplicador, '=', resultado)
    multiplicador += 1

