import numpy as np
def sol_Array(datos,n_Datos):
    A = np.zeros((n_Datos,n_Datos))
    for i in range(0,n_Datos):
        for k in range(0,n_Datos):
            A[i][k] = pow(datos[0][i],n_Datos-k-1)
    return A

def sol_Res(datos,n_Datos):
    b = np.zeros((n_Datos))
    for j in range(0,n_Datos):
        b[j] = datos[1][j]
    return b