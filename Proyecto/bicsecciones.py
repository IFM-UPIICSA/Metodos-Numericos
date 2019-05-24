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
contador = 0
X1 = []
X2 = []
Xmedia = []
fX1 = []
fX2 = []
fXmedia = []
error_value = []
    #Primeros calculos
X1.append(x1)
X2.append(x2)
Xmedia.append((x1+x2)/2)
    #Calcular f(X1)
temp = 0
for i in range(grade-1,-1,-1):
        if(i!=0):
            temp += ( function_value[i] * (X1[contador]**i))
        else:
            temp += (function_value[i])
fX1.append(temp) #Incrustar en el array
    #Calcular f(X2)
temp = 0
for i in range(grade-1,-1,-1):
        if(i!=0):
            temp += ( function_value[i] * (X2[contador]**i))
        else:
            temp += (function_value[i])
fX2.append(temp)
    #Calcular f(Xmedia)
temp = 0
for i in range(grade-1,-1,-1):
        if(i!=0):
            temp += ( function_value[i] * (Xmedia[contador]**i))
        else:
            temp += (function_value[i])
fXmedia.append(temp)
    #Actualizar valores
if(fXmedia[contador] < 0):
    X1.append(Xmedia[contador])
    X2.append(X2[contador])
else:
    X2.append(Xmedia[contador])
    X1.append(X1[contador])
    #Calcular el error
error_value.append(abs(fXmedia[0]))
    #Incrementar contador  
contador = contador+1

    #Iteraciones
while ( error_value[contador-1] > (5/(10**fix_value))):
        #Calcular Xmedia
    Xmedia.append((X1[contador]+X2[contador])/2)
        #Calcular fx1
    temp = 0
    for i in range(grade-1,-1,-1):
        if(i!=0):
            temp += ( function_value[i] * (X1[contador]**i))
        else:
            temp += (function_value[i])
    fX1.append(temp)
        #Calcular fx2
    temp = 0
    for i in range(grade-1,-1,-1):
        if(i!=0):
            temp += ( function_value[i] * (X2[contador]**i))
        else:
            temp += (function_value[i])
    fX2.append(temp)
        #Calcular fXmedia
    temp = 0
    for i in range(grade-1,-1,-1):
        if(i!=0):
            temp += ( function_value[i] * (Xmedia[contador]**i))
        else:
            temp += (function_value[i])
    fXmedia.append(temp)
        #Actualizar valores
    if(fXmedia[contador] < 0):
        X1.append(Xmedia[contador])
        X2.append(X2[contador])
    else:
        X2.append(Xmedia[contador])
        X1.append(X1[contador])
        #Calcular error
    error_value.append(abs(fXmedia[contador]))
        #Incrementar contador  
    contador = contador+1
        ################ Finaliza el while
    #Crear y llenar tabla
tabla = []
for i in range(len(error_value)):
    temp1 = round(X1[i],fix_value)
    temp2 = round(X2[i],fix_value)
    temp3 = round(Xmedia[i],fix_value)
    temp4 = round(fX1[i],fix_value)
    temp5 = round(fX2[i],fix_value+1)
    temp6 = round(fXmedia[i],fix_value+1)
    temp7 = round(error_value[i],fix_value+1)
        #agregar al array
    tabla.append([i, temp1, temp2, temp3, temp4, temp5, temp6, temp7])
    #Barra titular
print("\n\t\tResultado:")
print("\nn\tX1\tX2\tXmedia\tf(X1)\tf(X2)\tf(Xmedia)\tError |f(Xmedia)|\n")
    #Imprimir tabla
for i in range(len(X1)-1):
    print(tabla[i])
print("\n"*3) #Espaciado