##############################################
# ISMAEL FLORES MELÉNDEZ
# 11/03/19
# Solución de una intepolación de grado 3
##############################################

# imports
import numpy
from gauss_method import gaussJordan

    #Declaraciones
# Matriz de coeficientes
A = [ [ 2.56, 1.6, 1], [ 3.24, 1.8, 1], [ 1.96, 1.4, 1] ]
# Matriz de resultados
b = [1.6487,2.7182,1]
# Valor a calcular
x = 1.7

    # Resolución de la matriz por Gauss Jordan
R = (gaussJordan(A, b))
print(R)

    # Realizar el calculo del valor en función de los valores de la matriz
    # y el polinomio a emplear
# Polinomio de grado 3
Resultado = ( R[0]*(x**2) ) + ( R[1]*(x) )+ ( R[2] )
print(round(Resultado,4))