#contador de vocales
import os
controlBln = True
a = 0
e = 0
i= 0
o= 0
u = 0
total_vocales = 0

while controlBln == True:
    os.system('cls')
    letraStr = (input('Ingrese alguna letra o vocal\n2.Finalizar->\n')) 
    if letraStr == 'a':
        a += 1
        total_vocales += 1
    if letraStr == 'e':
        e += 1
        total_vocales += 1
    if letraStr == 'i':
        i += 1
        total_vocales += 1
    if letraStr == 'o':
        o += 1
        total_vocales += 1
    if letraStr == 'u':
        u += 1
        total_vocales += 1
        os.system('cls')
    if letraStr == '2':
        controlBln = False
        print('El total de vocales fueron:' , total_vocales)
        print('la cantidad de A fueron:' , a)
        print('la cantidad de E fueron:' , e)
        print('la cantidad de I fueron:' , i)
        print('la cantidad de O fueron:' , o)
        print('la cantidad de U fueron:' , u)
        
        
    
    
    