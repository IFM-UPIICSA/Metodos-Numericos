    #imports
import numpy as np
from funciones.solitud_datos import sol_tabla_33, sol_array_3
    #Diferent Values
change = []
VLI_items = [False,False,False]
tabla_cal = np.zeros((9,3))
tabla_err = np.zeros((9,3))
 
    #Error message by item, number, descripcions
def MensajesError(num):
    print("La fila ",num," no cumple la regla de linealidad")

    # Linealmente independiente
def VerifyLinealIndep():   
    print() 
        #Validate Column zero
    if ( (abs(tabla_mat[0][0])) < ( abs(tabla_mat[0][1]) + abs(tabla_mat[0][2])) ):
        MensajesError(0)
        VLI_items[0] = False
        change.append(0)
    else: VLI_items[0] = True

        #Validate Column one
    if ( (abs(tabla_mat[1][1])) < ( abs(tabla_mat[1][0]) + abs(tabla_mat[1][2])) ):
        MensajesError(1)
        VLI_items[1] = False
        change.append(1)
    else: VLI_items[1] = True

        #Validate Column two
    if ( (abs(tabla_mat[2][2])) < ( abs(tabla_mat[2][1]) + abs(tabla_mat[2][0])) ):
        MensajesError(2)
        VLI_items[2] = False
        change.append(2)
    else: VLI_items[2] = True

def VerifyAllLinealIndep():
        #Validate All rows
    if ( (VLI_items[0]==True) and (VLI_items[1]==True) and (VLI_items[2]==True) ): 
        return True
    else: 
        return False

    #Try to fix order of matrix
def RepairIndependence():
    for i in range(0,3):
            #tabla_mat
        temp = tabla_mat[change[0]][i]
        tabla_mat[change[0]][i] = tabla_mat[change[1]][i]
        tabla_mat[change[1]][i] = temp
            #tabla_res
        temp = tabla_res[change[0]]
        tabla_res[change[0]] = tabla_res[change[1]]
        tabla_res[change[1]] = temp
    print("\nTabla de datos con intercambio de filas")
    print(tabla_mat)
    print("\nTabla de resultados con intercambio de filas")
    print(tabla_res)

def main():
    VerifyLinealIndep()
    if VerifyAllLinealIndep() == True:
        print("\nLa matriz cumple la regla de linealidad")
    else: 
        if(len(change)%2 == 0):
            RepairIndependence()
            VerifyLinealIndep()
            if VerifyAllLinealIndep() == True:
                print("\nLa matriz cumple la regla de linealidad\n")
                return True
            else: 
                print("\nLa matriz no cumple la regla de linealidad, no pudo ser reparada por lo que no tiene solución por jacobic")    
                return False
        else:
            print("\nLa matriz no cumple la regla de linealidad, y dados sus valores no tiene solución por jacobic")
            return False

def calc_inc():
    x = []
    x.append(( ( tabla_res[0] + ((-1)*(tabla_mat[0][1])) + ((-1)*(tabla_mat[0][2])) ) ) / (tabla_mat[0][0]))
    x.append(( ( tabla_res[1] + ((-1)*(tabla_mat[1][0])) + ((-1)*(tabla_mat[0][2])) ) ) / (tabla_mat[1][1]))
    x.append(( ( tabla_res[2] + ((-1)*(tabla_mat[2][0])) + ((-1)*(tabla_mat[2][1])) ) ) / (tabla_mat[2][2]))
    print ("X1= ",x[0])
    print ("X2= ",x[1])
    print ("X3= ",x[2])
    return (x)

def calc_tabla(x):
        #declaraciones
    tabla_cal[1][0] = x[0]
    tabla_cal[1][1] = x[1]
    tabla_cal[1][2] = x[2]
    tabla_err[1][0] = 1
    tabla_err[1][1] = 1
    tabla_err[1][2] = 1
        #calculos rangos
    for i in range(2,9):
        tabla_cal[i][0] = ( ( tabla_res[0] - ((tabla_mat[0][1])*(tabla_cal[i-1][1])) - ((tabla_mat[0][2])*(tabla_cal[i-1][2])) ) / (tabla_mat[0][0]) )
        tabla_cal[i][1] = ( ( tabla_res[1] - ((tabla_mat[1][0])*(tabla_cal[i-1][0])) - ((tabla_mat[1][2])*(tabla_cal[i-1][2])) ) / (tabla_mat[1][1]) )
        tabla_cal[i][2] = ( ( tabla_res[2] - ((tabla_mat[2][0])*(tabla_cal[i-1][0])) - ((tabla_mat[2][1])*(tabla_cal[i-1][1])) ) / (tabla_mat[2][2]) )
        #calculos error
    for j in range(2,9):
        tabla_err[j][0] = abs( (tabla_cal[j-1][0] - tabla_cal[j][0])  / (tabla_cal[j][0]) )
        tabla_err[j][1] = abs( (tabla_cal[j-1][1] - tabla_cal[j][1])  / (tabla_cal[j][1]) )
        tabla_err[j][2] = abs( (tabla_cal[j-1][2] - tabla_cal[j][2])  / (tabla_cal[j][2]) )
        #concatenar tabla
    tabla_fin = np.concatenate((tabla_cal,tabla_err), axis=1)
        #Impresion tabla
    print("\n\t\tTabla de Xs\t\t\tTabla de Error")
    print(tabla_fin)

#Main
print("\n\tMetodo de Jacobic\n")
tabla_mat = sol_tabla_33()
tabla_res = sol_array_3()
print("\nTabla de datos")
print(tabla_mat)
print("\nTabla de resultados")
print(tabla_res)
if(main()==True):
    calc_tabla(calc_inc())