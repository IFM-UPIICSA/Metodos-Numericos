# Interpolacion polinomica de Lagrange
    #Imports
import numpy as np
from metodos.solitud_datos import sol_Value_Calcular

print("\n\tINTERPOLACION POLINOMICA DE LAGRANGE\n\n")

def prod(A):
    a = 1
    for i in range(len(A)):
        a = a*A[i]
    return a

def main():
        #Definir matrices
    pun_Con = int(input("Ingrese cantidad de datos conocidos > 2: "))
    datos = np.arange(pun_Con*2,dtype=float)
    lfun = np.arange((pun_Con)**2,dtype=float)
    datos.shape = (2,pun_Con)
    lfun.shape = (pun_Con,pun_Con)
        
        #Ingreso de valores
    print("\nIngrese los valores\n")
    for i in range(pun_Con):
        datos[0,i] = float(input(f"Ingrese X{i}: "))
        datos[1,i] = float(input(f"Ingrese Y{i}: "))

        #Solicitud del valor a calcular
    pun_des = float(sol_Value_Calcular())

        #Estructuración de valores
    for i in range(len(datos[0])):
        for j in range(len(lfun)):
            if i == j:  lfun[i,j] = 1
            else:  lfun[i,j] = (pun_des-datos[0,j])/(datos[0,i]-datos[0,j])

        #Calculo de resultado
    resultado = []
    for i in range(len(datos[1])):
        resultado.append(prod(lfun[i])*datos[1,i])

    res = sum(resultado)
    print ("\nResultado: Y para X =",pun_des," :",round(res,9),"\n\n")

        #Calcular Polinomio de la tabla
    print("\t\t\tCalculo del polinomio de la tabla")
    VR = []
    for i in range(0,pun_Con):
        temp = 1
        for j in range(0,pun_Con):
            if(i!=j): temp *= ((datos[0][i])-(datos[0][j]))
        VR.append( (datos[1][i]) / (temp) ) 
    print("VR")
    print(VR)

        #Calcular x^2
    X2 = 0
    for k in range(0,pun_Con):
        X2 += VR[k]
    
        #Calcular x^1
    X1 = 0
    for jj in range(0,pun_Con):
        temp2 = 0
        for kk in range(0,pun_Con):
            if(jj!=kk): temp2 -= ( datos[0][kk] )
        X1 += (temp2*VR[jj])        

        #Calcular x^0
    X0 = 0
    for ij in range(0,pun_Con):
        temp3 = 1
        for jk in range(0,pun_Con):
            if(ij!=jk): temp3 *= ( -datos[0][jk] )
        X0 += (temp3*VR[ij])  

        #Imprimir resultados
    print("\nX^2 : ",X2)
    print("X^1 : ",X1)
    print("X^0 : ",X0)
    #main
main()