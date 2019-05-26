#############################
#                           #
#       Metodo              #
#       Estadistico         #
#                           #
#############################
    #Imports
import numpy as np
from funciones.solitud_datos import sol_tabla_2n
from funciones.solitud_datos import sol_No_Datos
from funciones.solitud_datos import sol_Value_Calcular
from funciones.solitud_datos import enters
from funciones.solitud_datos import function_grade_n

    #Presentacion
def Presentacion():
    print("\n"*3)
    print("*"*33)
    print("*"+(" "*31)+"*")
    print("*"+(" "*7) + "Metodo Estadistico" + (" "*6)+"*")
    print("*"+(" "*31)+"*")
    print("*"*33)

def SolTabla(tabla, grade, num_datos):
    tabla_completa = [] #Calc columnas => ( 2 + ( (grade*2) -3 ) + (grade - 2) )
    for i in range(0 , num_datos):
        temp_tabla = []
        temp_tabla.append(tabla[0][i])
        temp_tabla.append(tabla[1][i])
        for j in range(2, ( (grade*2) -3 )):
            temp_dato = ((tabla[0][i])**j)
            temp_tabla.append(temp_dato)
        for j in range(1, (grade - 2)+1 ):
            temp_dato = ((tabla[0][i]**j)*tabla[1][i])
            temp_tabla.append(temp_dato)
        tabla_completa.append(temp_tabla)
    return tabla_completa

def Calc_Tabla_Totales(tabla_completa, num_datos):
    tabla_totales = []
    for i in range (0, num_datos):
        temp_dato = 0
        for j in range (0, num_datos):
            temp_dato += tabla_completa[j][i]
        tabla_totales.append(temp_dato)
    return tabla_totales
    
def ImprimirTablas(tabla_completa, tabla_totales, num_datos):
    print("\tTabla de Resultados:\n  X  | Y |   X^n         |  X^n*Y")
    for i in range (0,num_datos):
        print(tabla_completa[i])
    print("\tTotales:")
    print(tabla_totales)

    #Inicio del Metodo
def MethodEstadistico(): 
    Presentacion()
    enters(1)
    num_datos = sol_No_Datos() #Solicitar el numero de datos
    enters(1)
    tabla = sol_tabla_2n(num_datos) #solicitud de datos
    enters(1)
    valor_calcular = sol_Value_Calcular() #Solicitud del valor a calcular
    enters(1)
    print("Valores ingreasados:\n")
    print(tabla)
        #Ingrese el grado de la funcion
    print("\n\tDefina la función: \n")
    grade = int(input("Ingrese el grado de la funcion: "))+1
        #Resolver tabla
    tabla_completa = SolTabla(tabla, grade, num_datos)
        #Calcular totales
    tabla_totales = Calc_Tabla_Totales(tabla_completa,num_datos)
        #Imprimir tabla
    enters(1)
    ImprimirTablas(tabla_completa, tabla_totales, num_datos) 

MethodEstadistico()