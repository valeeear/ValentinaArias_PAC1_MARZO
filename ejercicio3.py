#conversor de temperatura

while  True:
    temperatura = float(input('Ingrese la temperatura->'))
    opcionStr = input('\n1Ingreser la unidad de medida:C. celsius, F. fahrenheit\n2.Finalizar\n')
    if opcionStr == 'C' or opcionStr == 'c':
        gradosfahrenheit = (temperatura * 9/5) +32
        print(temperatura, 'grados celsius son equivalentes a' , gradosfahrenheit, 'grados fahrenheit')
    if opcionStr == 'F' or opcionStr == 'f':
        gradoscelsius = (temperatura - 32) * 5/9
        print(temperatura, 'grados fahrenheit son equivalentes a ', gradoscelsius, 'grados celsius')
    if opcionStr == '2':
        break