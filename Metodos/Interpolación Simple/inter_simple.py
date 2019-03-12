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

    # Resolución de la matriz
R = (gaussJordan(A, b))
print(R)