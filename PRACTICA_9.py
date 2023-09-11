'''
Hacer un programa que lea nombre ,precio y cantidad de un producto  datos validados , donde el usuario determinara
 cunatos productos se van a introduccior y al finalizar mostrata sin iva , el iva del total y total a pagar 
'''
def validadNumero(Numeros):
    if Numeros.isdigit(): 
        return True
    else:
        return False
    



def validarLetra(Nombre):
    if Nombre.isalpha(): 
        return True
    else:
        return False

def pedirDatos():
    
    global Total
    global Numeros 
    Numeros = ""
    global Nombre 
    Nombre = ""
    global Precio 
    Precio = 0
    global Cantidad 
    Cantidad = 0 

    while(True):
     Nombre = input ('Escribe un producto\n')
     res =  validarLetra(Nombre)
     if res == True:
            break
     else :
            print('Error no es nombre de producto')
    while (True):
        Numeros = input ('Escribe el precio\n')
        res = validadNumero(Numeros)
        if res == True:
            Precio = int (Numeros)
            break
        else : 
            print('Error no es precio de producto') 
    while(True):
        Numeros =  input('Escribe la cantidad\n')
        res = validadNumero(Numeros)
        if res == True:
            Cantidad = int(Numeros)
            Total += Cantidad * Precio
            break
        else:
           print('Error no es cantidad de producto')  

    

    
    

global Numeros 
global Nombre 
global Precio 
global Cantidad 
global Total 
Total = 0 
while(True):
    pedirDatos()
    r = input('Deseas otro producto\n')
    if not r == 'Si':
        print ('El total: ' , Total)
        IVA = Total * 0.16
        print('El IVA total es:' , IVA )
        TIVA = Total + IVA 
        print('Compra total es: ', TIVA)
        break


#print ('El prodcuto {0} con precio {1} y la cantidad de {2} productos'.format(Nombre,Precio,Cantidad))
