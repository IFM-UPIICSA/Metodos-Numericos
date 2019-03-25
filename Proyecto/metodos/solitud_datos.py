import numpy as np

def sol_No_Datos():
    num_Datos = int(input("Ingresa el número de datos: "))
    return num_Datos

def sol_Value_Calcular():
    y = (input("Ingrese el valor a calcular: "))
    return y

def sol_tabla(n_Datos):
    tabla = np.zeros((2,n_Datos))
    for i in range(0,n_Datos):
        tabla[0][i] = input(f"Ingrese el valor de X{i}: ")
        tabla[1][i] = input(f"Ingrese el valor de Y{i}: ")
    return tabla