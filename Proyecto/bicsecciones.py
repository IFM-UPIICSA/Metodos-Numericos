#############################
#                           #
#   Metodo de Bisecciones   #
#                           #
#############################

    #Imports
import numpy as np
from funciones.solitud_datos import sol_No_Datos
    #Titulo
print("Metodo de Bisecciones")

    #Solicitud de datos
print("\n\tDefina la función:\n")
x_cuadrada = (int(input("Ingresa el valor de X^2: ")))
x_uno = (int(input("Ingresa el valor de X^1: ")))
x_cero = (int(input("Ingresa el valor de X^0: ")))
print("\n\tIngrese el limite:\n")
x_inf = (int(input("Ingresa el valor inferior: ")))   
x_sup = (int(input("Ingresa el valor superior: ")))

    #Imprimiendo la funcion deseada
print("\nFuncion: \n\t(",x_cuadrada,"X^2) + (",x_uno,"X) +(",x_cero,")")
print("\nLimites: \n\t[",x_inf,",",x_sup,"]")

