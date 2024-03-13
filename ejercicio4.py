import os
ferreteriaFlt = 0.10
aseoFlt = 0.05
seguridadFlt = 0.15
alimentosFlt = 0.08
electrodomesticosFlt = 0.12


ferreteria_recaudo = 0
aseo_recaudo = 0
seguridad_recaudo = 0
alimentos_recaudo= 0
electrodomesticos_recaudo = 0

total_recaudado = 0
    
nombre = input('Ingrese su nombre->')


while True:
    categoriaStr = input('<<<MENÙ DE OPCIONES>>>\n1.Producto de ferreteria\n2. Producto de aseo\n3. Producto de seguridad\n4. Alimetos\n5. Electrodomesticos\n6.Finalizar\n')
    precioInt= int(input('¿Cual es el precio del producto?'))
    os.system('cls')

    if categoriaStr == '1':
        descuentofe = precioInt * ferreteriaFlt
        print('Tienes un descuento de' , descuentofe)
        preciofinalfe = precioInt - descuentofe
        print('El precio final del producto es->', preciofinalfe)
        ferreteria_recaudo += 1
        total_recaudado += 1
    if categoriaStr == '2':
        descuentoase = precioInt * aseoFlt
        print('Tienes un descuento de' , descuentoase)
        preciofinalase = precioInt - descuentoase
        print('El precio final del producto es->' , preciofinalase)
        aseo_recaudo += 1
        total_recaudado += 1
    if  categoriaStr == '3':
        descuentoseg = precioInt * seguridadFlt
        print('Tienes un descuento de' , descuentoseg)
        preciofinalseg = precioInt -descuentoseg
        print('El precio final del prodcuto es->' ,preciofinalseg)
        seguridad_recaudo += 1
        total_recaudado += 1
    if categoriaStr == '4':
        descuentoali = precioInt * alimentosFlt
        print('Tienes un descuento de' , descuentoali)
        preciofinalali = precioInt - descuentoali
        print('El precio final del producto es->' ,preciofinalali)
        alimentos_recaudo += 1
        total_recaudado += 1
    if categoriaStr == '5':
        descuentoele = precioInt * electrodomesticosFlt
        print('Tienes un descuento de' , descuentoele)
        preciofinalele  = precioInt - descuentoele
        print('El precio final del prodcuto es->' ,preciofinalele)
        electrodomesticos_recaudo += 1
        total_recaudado += 1
    if categoriaStr == '6':
        os.system('cls')
        print('>>>>REPORTE<<<<')
        print(nombre)
        print('Impletos de ferreteria fueron:..........' , ferreteria_recaudo)
        print('Implemetos de aseo fueron:..............' ,aseo_recaudo)
        print('Implemetos de seguridad fueron:.........' , seguridad_recaudo)
        print('Implemetos de alimetacion fueron:.......' , alimentos_recaudo)
        print('Implemetos electrodomesticos) fueron:...' , electrodomesticos_recaudo)
        print('El total de todos los productos comprados fueron:' , total_recaudado)
        
        break
    



