#############################
#                           #
#   Metodo de Bisecciones   #
#                           #
#############################

    #Imports
import numpy as np
from funciones.solitud_datos import sol_No_Datos, function_grade_n

    #Titulo
print("*"*33)
print("*"+(" "*31)+"*")
print("*"+(" "*5) + "Metodo de Bisecciones" + (" "*5)+"*")
print("*"+(" "*31)+"*")
print("*"*33)
    #Solicitud de datos
print("\n\tDefina la función: \n")
grade = int(input("Ingrese el grado de la funcion: "))+1
function_value = function_grade_n(grade)
print("\n\tIngrese el limite:\n")
x1 = (int(input("Ingresa el valor inferior: ")))   
x2 = (int(input("Ingresa el valor superior: ")))
    #Imprimiendo datos ingresados
print("\n\tFuncion:\n")
for i in range(grade-1,-1,-1):
    if(i!=0):
        print("X^",i," = ",function_value[i])
    else:
        print("Termino independiente = ", function_value[i])
print("\n\tLimites: \n[",x1,",",x2,"]")
    #Solicitud del fix
fix_value= (int(input("\nIngrese el fix: ")))
        #Calcular y mostrar las iteraciones
    #Definicion de variables
error_value = 1
contador = 0
    #Barra titular
print("n\tX1\t\tX2\tXmedia\tf(X1)\tf(X2)\tf(Xmedia)\tError |f(Xmedia)|")
    #Iteraciones
while ( error_value > (5/(10**fix_value))):
        #Init values
    Xmedia = 0
    fX1 = 0
    fX2 = 0
    fXmedia = 0
        #Calcular Xmedia
    Xmedia = ( (x1+x2) / 2 )
        #Calcular fx1
    for i in range(grade-1,-1,-1):
        if(i!=0):
            fX1 += ( function_value[i] * (x1**i))
        else:
            fX1 += (function_value[i])

        #Calcular fx2
    for i in range(grade-1,-1,-1):
        if(i!=0):
            fX2 += ( function_value[i] * (x2**i))
        else:
            fX2 += (function_value[i])

        #Calcular fXmedai
    for i in range(grade-1,-1,-1):
        if(i!=0):
            fXmedia += ( function_value[i] * (Xmedia**i))
        else:
            fXmedia += (function_value[i])

        #Calcular error
    error_value = abs(fXmedia)

        #Imprimir iteracion
    print(contador,"\t",round(x1,fix_value),"\t",round(x2,fix_value),"\t",round(Xmedia,fix_value),"\t",round(fX1,fix_value),"\t",round(fX2,fix_value),"\t",round(fXmedia,fix_value),"\t\t",round(error_value,fix_value))
    if(fXmedia < 0):
        x1 = Xmedia
    else:
        x2 = Xmedia
    
    contador = contador+1
    