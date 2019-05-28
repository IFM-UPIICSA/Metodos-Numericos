import numpy as np
from funciones.solitud_datos import enters, sol_array_3, sol_tabla_33, sol_Value_Calcular
from funciones.gauss_method import gaussJordan
from funciones.calcular_matrices import sol_Array, sol_Res
def GaussJordan():    
    print("\n"*3)
    print("*"*32)
    print("*"+(" "*30)+"*")
    print("*"+(" "*9) + "Gauss Jordan" + (" "*9)+"*")
    print("*"+(" "*30)+"*")
    print("*"*32)
        #Solicitud de datos
    matriz_A = sol_tabla_33()
    enters(1)
    matriz_b = sol_array_3()
    print("\nMatriz A")
    print(matriz_A)
    print("\nMatriz b")
    print(matriz_b)
        # Resolución de la matriz por Gauss Jordan
    R = (gaussJordan(matriz_A, matriz_b))
    print("\nSolición de la matriz por Gauss Jordan")
    print(R)
    enters(2)