'''
Hacer un programa que muestre en pantalla un menú 
1 Área de un cuadrado
2 Área de un círculo
3 Área de un triángulo
Dependiendo de la opción del menú se pedirá los datos correspondientes para calcular el área
'''
res = 'si'
while(res == 'si'):
    print (" Elige una opcion para resolver ")
    print(" 1 Area de un cuadrado")
    print(" 2 Area de un círculo ")
    print(" 3 Area de un triángulo")

    op = input ( 'Dime una opccion  ')

    if  op == '1' :
        l = int(input( 'Dime el lado del cuadrado  ' ))
        a = l * l
        print ('El area es : ' ,a)
    
    elif op == '2':
        r = int(input( 'Dime el radio del circulo ' ))
        are = 3.1416 * (r**2)
        print ('El area es : ' , are)


    elif op == '3':
        b = int(input (" Dime la base del triangulo  "))    
        a = int(input( "Dime la altura del triangulo " ))
        area = b * a / 2
        print ('El area es : ' ,area)

    else : 
        print('Opccion incorrecta')
    res = input ('Lo quieres intentar otra vez \n ')
