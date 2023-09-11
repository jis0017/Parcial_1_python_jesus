 
'''hacer un programa que muestre el siguiente menu
1 suma
2 resta
3 multiplicacion
4 division con decimales
5 division en entero 
6 potencia 
7 raiz
'''
#APLICACION DE METODDOS

def Menu ():
    print ('1 suma')
    print ('2 resta')
    print ('3 multiplicacion')
    print ('4 division con decimales')
    print ('5 division con enteros')
    print ('6 potencia')
    print ('7 raiz')
    print ('8 salir')

def suma():
    a = int(input('Escribe un numero:\n'))
    b = int(input('Escribe otro numero:\n'))
    print('El resultado de la suma es: ', a+b)
def resta():
    a = int(input('Escribe un numero:\n'))
    b = int(input('Escribe otro numero:\n'))
    print('El resultado de la resta es: ', a-b)
def division():
    a = float(input('Escribe un numero:\n'))
    b = float(input('Escribe otro numero:\n'))
    print('El resultado de la division con decimales es: ', a/b)
def raiz():
    a = int(input('Escribe un numero:\n'))
    r = a ** (1/2)
    print('La raiz del numero es:', r)
def divis():
    a = int(input('Escribe un numero:\n'))
    b = int(input('Escribe otro numero:\n'))
    print('El resultado de la division es: ', a//b)
def pote():
    a = int(input('Escribe un numero:\n'))
    b = int(input('Escribe el numero al la potencia:\n'))
    print('El resultado de la potencia es: ', a**b)
def multi():
    a = int(input('Escribe un numero:\n'))
    b = int(input('Escribe otro numero:\n'))
    print('El resultado de la suma es: ', a*b)
while(True):
    Menu ()
    op = int(input ('Elige una opcion:\n'))
    if op == 1:
        suma()
    if op == 2:
        resta()
    if op == 7:
        raiz()
    if op == 3:
        multi ()
    if op == 4:
        division()
    if op == 5:
        divis()
    if op == 6:
        pote()
    if op == 8:
        break
    elif op > 8 or op < 1:
        print('Escribe una opcion dentro del menu')