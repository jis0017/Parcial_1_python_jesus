"""
HACER UN PROGRMAMA QUE EN UN ARREGLO DE STRIN DE 7 POCICONES SE PIDA SE VALIDE  SE  INTRODUCE Y 
SE PACE AL ARREFLO LOS DIAS DE LA SEMANA SIN REPETIR Y MOSTRAR
"""
semana = []
def validardias(Dias):
    if Dias.isalpha(): 
        return str
    else:
        return print("No es una dia de la semana")

a = ""
b = range(0,7)



def dias_semana ():
    
    while(True):
     Dias =  input ("Ingresa el una dia de la semana \n ")
     vali = validardias(Dias)
     if vali == True: 
            break
     if Dias in dias_semana:
            print("Este dia ya esta guardado  Introduce otro ")
     elif Dias not in ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]:
            print("Dia no válido , dime  un día de la semana correcto")
     