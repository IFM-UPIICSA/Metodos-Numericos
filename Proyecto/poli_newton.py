#############################
#                           #
#       Polinomio           #
#       de Newton           #
#                           #
#############################
    #Imports
import numpy as np
from funciones.solitud_datos import enters
from funciones.solitud_datos import sol_tabla_2n, sol_No_Datos

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
        print("\n\nTabla de Iteraciones:")
        print(tabla_values)

PoliNewton()