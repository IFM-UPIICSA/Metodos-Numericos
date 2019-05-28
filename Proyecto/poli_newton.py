#############################
#                           #
#       Polinomio           #
#       de Newton           #
#                           #
#############################
    #Imports
import numpy as np
import math
from funciones.solitud_datos import enters
from funciones.solitud_datos import sol_tabla_2n, sol_No_Datos, sol_Value_Calcular

def Presentacion():
    enters(2)
    print("*"*31)
    print("*"+(" "*29)+"*")
    print("*"+(" "*10) + "Polinomio" + (" "*10)+"*")
    print("*"+(" "*10) + "de Newton" + (" "*10)+"*")
    print("*"+(" "*29)+"*")
    print("*"*31)
    enters(2)

def validar_H(init_tabla, num_data):
    h_value = init_tabla[0][1] - init_tabla[0][0]
    value_return = True
    for i in range (0, num_data-1):
        if( h_value != (init_tabla[0][i+1] - init_tabla[0][i]) ):
            value_return = False
            break
    return value_return

def Contruction_Table(init_table, num_data):
    tabla_creation = np.zeros((num_data, num_data+1)) #create matriz
    for i in range (0, num_data): #llenar con datos iniciales
        tabla_creation[i][0] = init_table[0][i]
        tabla_creation[i][1] = init_table[1][i]
    for i in range(1, num_data):
        for j in range(2, num_data+1):
            if(j<=i+1):
                tabla_creation[i][j] = (tabla_creation[i][j-1]-tabla_creation[i-1][j-1])
    return tabla_creation

def Search_Menor(tabla_values, value_calcular, num_data):
    menor = tabla_values[0][0]
    for i in range(0, num_data):
        if((value_calcular>tabla_values[i][0])):
            menor = tabla_values[i][0]
        else:
            break
    return menor

def Buscar_Inicio(tabla_values, menor, num_data):
    inicio = 0
    for i in range(0, num_data):
        if( menor == tabla_values[i][0] ):
            inicio = i
            break
    return inicio

def Calcular_Dividendo(k, num_veces):
    valor_calculado = k
    if num_veces>1:
        for ii in range (1, num_veces):
            valor_calculado *= (k-ii)
    return float(valor_calculado)

def Calcular_Result(tabla_values, value_calcular, num_data):
    result = 0 #definir resultado
    menor = Search_Menor(tabla_values, value_calcular, num_data) #calcular menor
    k = round( (value_calcular-menor)/(tabla_values[1][0] - tabla_values[0][0]),5) #calcular k
    print("\nMenor: ",menor," K: ",k)
        #Calcular el inicio de la tabla
    inicio = Buscar_Inicio(tabla_values, menor, num_data)
        #Sumar resultados
    result = tabla_values[inicio][1] #default
    num_veces = 1
    print("\nTabla de Resultados por iteracion: ")
    for i in range(inicio+1, num_data):
        result += ( ( (Calcular_Dividendo(k, num_veces))/(float(math.factorial(num_veces))) ) * (tabla_values[i][num_veces+1]) )
        print("Iteracion:",(i-2),", resultado =",result)
        num_veces = num_veces+1
    return result

    #Metodo de Bisecciones
def PoliNewton(): 
    Presentacion()
        #Require Data
    num_data = sol_No_Datos()
    enters(2)
    init_tabla = sol_tabla_2n(num_data)
    print("\n\nValores Ingresados:")
    print(init_tabla)
    validation = validar_H(init_tabla, num_data)
    if(validation == False):
        print("\n\n\tNo cumple con la regla de simetria de las H\n\n\tpor lo que no tiene solucion por este metodo\n\n")
    else:
        tabla_values = Contruction_Table(init_tabla, num_data)
        print("\n\nTabla de Calculos:")
        print(tabla_values)
        value_calcular = float(sol_Value_Calcular())
        result = Calcular_Result(tabla_values, value_calcular, num_data)
        print("\n\nEl resultado final para ",value_calcular," es = ",result)
        enters(2)