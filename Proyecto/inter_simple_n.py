##############################################
# ISMAEL FLORES MELÉNDEZ
# 25/03/19
# Solución de cualquier grado de intepolación 
##############################################

    # imports
import numpy as np
from funciones.gauss_method import gaussJordan
from funciones.solitud_datos import sol_tabla_2n, sol_No_Datos, sol_Value_Calcular, enters
from funciones.calcular_matrices import *

def InterSimple():
    print("\n"*3)
    print("*"*33)
    print("*"+(" "*31)+"*")
    print("*"+(" "*6) + "Intepolacion Simple" + (" "*6)+"*")
    print("*"+(" "*31)+"*")
    print("*"*33)
        #Ingresar el maximo grado de polinomio a calcular
    enters(1)
    Ngrado = sol_No_Datos()
        #Solicitud de datos
    enters(1)
    tabla = sol_tabla_2n(Ngrado)
    print("\n\nTabla de datos")
    print(tabla)
    #definir las matrices
    print("\nMatriz A")
    A = np.array(sol_Array(tabla,Ngrado), dtype=np.float64)
    print(A)
    b = np.array(sol_Res(tabla,Ngrado), dtype=np.float64)
    print("\nMatriz b")
    print(b)
    #solicitar el valor a calcular
    print()
    x = sol_Value_Calcular()

        # Resolución de la matriz por Gauss Jordan
    R = (gaussJordan(A, b))
    print("\nSolición de la matriz por Gauss Jordan")
    print(R)

    #Calcular valor en función del polinomio más adecuado
    Res = 0
    for i in range(0, Ngrado): Res += (R[i]*pow(float(x),Ngrado-i-1))
    print("\nResultado del polinomio ", round(Res,9),"\n")