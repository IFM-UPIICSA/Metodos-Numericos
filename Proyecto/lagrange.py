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
    for ii in range(0,pun_Con):
        X2 += VR[ii]
    
        #Calcular x^1
    


        #Calcular x^0
    
        #Imprimir resultados
    print("\nX^2 : ",X2)
    #main
main()