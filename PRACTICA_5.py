'''crear un programa que lea el nombre y el precio de un producto, el 
 repetira esta accion hasta que el usuario lo desee 
y al finalizar mostrara el total de productos, la sumatoria de los precios
, el porcentaje de IVA respecto al total y el total a pagar
'''
pro = 'Si'
n = 0
p = 0
while(pro =='Si' ):  
  input('Escriba el nombre de su producto')
  pr = int(input('Escriba el precio del producto'))
  
  n += 1
  p += pr


  pro = input('quiere seguira agregando productos (Si/No)\n')
  
print ('el total de productos son:' ,n )
print ('El total sera : ' , p)
print ('total a pagar es:', p*1.16)
print ('IVA total es:', p*0.16)




 