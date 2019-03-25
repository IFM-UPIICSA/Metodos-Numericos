##############################################
# ISMAEL FLORES MELÉNDEZ
# 25/03/19
# Solución de cualquier grado de intepolación 
##############################################

# imports
import numpy as np
from metodos.gauss_method import gaussJordan
from metodos.solitud_datos import *
from metodos.calcular_matrices import *

#Ingresar el maximo grado de polinomio a calcular
Ngrado = sol_No_Datos()
#Solicitud de datos
print()
tabla = sol_tabla(Ngrado)
print("\nTabla de datos")
print(tabla)
#definir las matrices
print("\nMatriz A")
A = np.array(sol_Array(tabla,Ngrado), dtype=np.float64)
print(A)
b = np.array(sol_Res(tabla,Ngrado), dtype=np.float64)
print()
print("Matriz b")
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