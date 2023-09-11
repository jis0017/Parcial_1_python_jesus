
def LeerDatos():
    a =input ('Escribe un valor')
    return a 
def validarDatos(a):
    if a.isdigit():
        return 'son numeros'
    else:
        return 'No son numeros'
b = LeerDatos()
print(validarDatos(b))
    