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
print("Defina la función")
x_cuadrada = (int(input("Ingresa el valor de X^2: ")))
x_uno = (int(input("Ingresa el valor de X^1: ")))
x_cero = (int(input("Ingresa el valor de X^0: ")))
    #Imprimiendo la funcion deseada
print("Funcion: (",x_cuadrada,"X^2) + (",x_uno,"X) +(",x_cero,")")
