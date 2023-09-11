''''hacer un progrma que lea tres numeros validados  
y muestre en pantalla el mayor menor y el de amedias'''

def leerDatos():
    a = input('Escribe un valor')
    return a

def validarDatos(a):
    if a.isdigit():
        return True
    else:
        return False

n1 = 0
n2 = 0
n3 = 0
while(True):
    a = leerDatos()    
    if (validarDatos(a)):
        print('Es un numero')
        n1 = int(a)
        break
    else:
        print('No es un numero, vuelvalo a introducir')
while(True):    
    b = leerDatos()
    if (validarDatos(b)):
        print('Es un numero')
        n2 = int(b)
        break
    else:
        print('No es un numero, vuelvalo a introducir')
        
while(True):    
    c = leerDatos()
    if (validarDatos(c)):
        print('Es un numero')
        n3 = int(c)
        break
    else:
        print('No es un numero, vuelvalo a introducir')

numeroMayor = 0
numeroMenor = 0
if n1 > n2 :
    if n1 > n3:
        print('El mayor es ',n1)
        numeroMayor = n1
    else: 
        print('El mayor es ',n3)
        numeroMayor = n3
elif n2>n3:
    print('El mayor es ',n2)
    numeroMayor = n2
else:
    print('El mayor es ',n3)
    numeroMayor = n3
    
if n1 < n2 :
    if n1 < n3:
        print('El menor es ',n1)
        numeroMenor = n1
    else: 
        print('El menor es ',n3)
        numeroMenor = n3
elif n2 < n3:
    print('El menor es ',n2)
    numeroMenor = n2
else:
    print('El menor es ',n3)
    numeroMenor = n3
    
if(n1 < numeroMayor and n1 > numeroMenor):
    print('el numero de a medias es: ',n1)
elif(n2 < numeroMayor and n2 > numeroMenor):
    print('el numero de a medias es: ',n2)
else:
    print('el numero de a medias es: ',n3)



