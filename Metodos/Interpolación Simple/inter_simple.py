##############################################
# ISMAEL FLORES MELÉNDEZ
# 11/03/19
# Solución de una intepolación de grado 3
##############################################

# imports
import numpy as np

    #Declaraciones
# Matriz de coeficientes
A = np.array( [ [2.56,1.6,1],[3.24,1.8,1],[1.96,1.4,1] ], np.int32)
# Matriz de resultados
b = np.array([1.6487,2.7182,1], np.int32)

    # Resolución de la matriz
# Verificar que la determinante no sea cero
if((np.linalg.det(A))!=0.0): 
    # Generación de matriz inversa
    B = np.linalg.inv(A)
    # Calcular la solución de la matriz
    print(np.dot(B, b))
else:
    print("\nLa matriz de coeficientes es singular\n")
    print("Por lo que no se puede encontrar una solución")