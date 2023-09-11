'''Hacer un programa que llene obligatoriamente un arreglo de numeros 
de 5 posiciones validados , al final debe mostrar cuantos pares e impares se encuentran en el arreglo '''

def validarNumero(n):
    if n.isdigit():
        return int(n)
    else:
        print('No es un numero')
        return 0

a = [0,0,0,0,0]
cp = 0
ci = 0
for i in range (0,5):
    b = validarNumero(input ('Escribe un valor\n'))
    if not b == 0:
        a[i] = b
    
for i in a:
    if i % 2 == 0:
        cp += 1
    else:
        ci += 1
for i in a:
    print(i)

print('Total de pares ', cp, ' y de impares' ,ci )