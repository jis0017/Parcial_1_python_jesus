#arreglos 


def validarNumero(n):
    if n.isdigit():
        return int(n)
    else:
        print('No es un numero')
        return 0

b = ""
a = [0,0,0,0,0,0,0,0,0,0,0]
pos = 0 
v = 0 
while(b==""):
    b= input('Escribe un valor\n')    
    v = validarNumero(b)
    if not v == 0:
         a[pos] = v 
         pos += 1
         res = input('Deseas otro valor\n')
         if res == 's':
            if pos >=9:
                print('Arreglo lleno')
                break
            b = ""
    
    else:
        b=""   

for i in a:
    if not i ==0:
     print (i)