# Resolviendo un sistema de ecuaciones utilizando
# matriz inversa utilizando la librería numpy.
# # # # # # # # # #
import numpy as np
# primero se declara la matriz de Coeficientes
# como valores de 32 bits
A = np.array([[ 1, -3, 1] , [1, 2, 3], [ -1, 9, 7]] , np.int32)
# seguido de la matriz de resultados
y = np.array([[ 2] , [5], [12] ], np.int32)
# Para calcular la inversa primero verificamos que
# la matriz sea no singular. Obtenemos el Determinante
# y verificamos que este sea distinto de cero
print("\n Tenemos el determinante de la matriz \n")
print(np.linalg.det(A))
if((np.linalg.det(A)) != 0.0 ):
    # Verificar que el determinante no sea cero
    print("\n Generamos la matriz Inversa \n")
    B = np.linalg.inv(A)
    print("\n Mostramos la multiplicación de y*inv(A) \n")
    print("\n lo cual resuelve la ecuación. \n")
    print(np.dot(B , y) )
    print(B.dtype)
else:
    print("\n La matriz de coeficientes es singular. \n")
    # Matriz singular
    print("\n No se puede encontrar una solución.\n")