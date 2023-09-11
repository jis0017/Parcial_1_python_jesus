# Estructura repetividas 
a = 'Hola'

for i in range (1,10): #rango de nuemro 

    print (i)

print(' ')

for i in a:   #para recorrer cadenas 
    print (i)

print(' ')

for i in (7,10): #recorrer una cantidad de numeros
    print (i)    

# hacer un programa ue lea 5 numeros y muestre en pantalla cuantos pares e impares hay
'''n1=0
imp=0
for i in range (0,5):
    a= int(input("Escribe un numero:"))
    if a % 2 == 0 :
        n1 = n1+1
    else:
        imp = imp+1
        print('Numeros pares:', n1)
        print('Numeros pares:', imp)'''
#Ejemplo del profe
'''p=0
b=0
for i in range (0,5):
    a = int(input('Escribe un numero:'))
if a % 2 == 0:
    p += 1
else:
    b += 1
    print('La cantidad de paers son:',p,' y los impares son:', b)'''

'''a = 0
p = 0 
y = 0
while (a < 5 ):
    v = int(input('Escribre un numero'))
    if v % 2 == 0:
        p += 1

    else:
        y += 1
    
    a += 1
print('La cantidad de paers son:',p,' y los impares son:', b)
'''