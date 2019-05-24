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
x_inf = (int(input("Ingresa el valor inferior: ")))   
x_sup = (int(input("Ingresa el valor superior: ")))
    #Imprimiendo datos ingresados
print("\n\tFuncion:\n")
for i in range(grade-1,-1,-1):
    if(i!=0):
        print("X^",i," = ",function_value[i])
    else:
        print("Termino independiente = ", function_value[i])
print("\n\tLimites: \n[",x_inf,",",x_sup,"]")

fix_value= (int(input("\nIngrese el fix: ")))
cantidad = 40
    #Calcular iteraciones
while ( cantidad > (5/(10**fix_value))):
    print("Previo: ",round(cantidad, fix_value))
    cantidad = cantidad/10
    print("Post: ",round(cantidad, fix_value))
print("\n\n\n")
print (round(cantidad,fix_value))
    #Imprimir tabla
#print("\n\nResultado:\n|Iteracion|X1|X2|Xmedia|f(X1)|f(X2)|f(Xmedia)|Error|\n")
