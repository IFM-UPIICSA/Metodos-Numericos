##############################################
# ISMAEL FLORES MELÉNDEZ
# 11/03/19
# Solución de una intepolación de grado 3
##############################################

# imports
import numpy
from funciones.gauss_method import gaussJordan

#Matriz de coeficientes
A = [[ 4.0960, 2.56, 1.6, 1] , [5.8320, 3.24, 1.8, 1], [ 2.7440, 1.96, 1.4, 1], [8, 4, 2, 1]]
# Matriz de resultados
b = [1.6487,2.7182,1, 7.3891]
# Valor a calcular
x = 1.9

    # Resolución de la matriz por Gauss Jordan
R = (gaussJordan(A, b))
print("\nSolición de la matriz por Gauss Jordan")
print(R)

    # Calculo del valor en función de los valores de la matriz y el polinomio a emplear
# Polinomio de grado 3
Resultado = ( R[0]*(x**3) ) + ( R[1]*(x**2) ) + ( R[2]*(x) )+ ( R[3] )
print("\nResultado del polinomio ", round(Resultado,8),"\n")