    #imports
import numpy as np
from metodos.solitud_datos import sol_tabla_33
    #Diferent Values
change = []
VLI_items = [False,False,False]
 
    #Error message by item, number, descripcions
def MensajesError(num):
    print("La fila ",num," no cumple la regla de linealidad")

    # Linealmente independiente
def VerifyLinealIndep():   
    print() 
        #Validate Column zero
    if ( (abs(tabla[0][0])) < ( abs(tabla[0][1]) + abs(tabla[0][2])) ):
        MensajesError(0)
        VLI_items[0] = False
        change.append(0)
    else: VLI_items[0] = True

        #Validate Column one
    if ( (abs(tabla[1][1])) < ( abs(tabla[1][0]) + abs(tabla[1][2])) ):
        MensajesError(1)
        VLI_items[1] = False
        change.append(1)
    else: VLI_items[1] = True

        #Validate Column two
    if ( (abs(tabla[2][2])) < ( abs(tabla[2][1]) + abs(tabla[2][0])) ):
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
        temp = tabla[change[0]][i]
        tabla[change[0]][i] = tabla[change[1]][i]
        tabla[change[1]][i] = temp
    print("\nTabla con intercambio de filas")
    print(tabla)

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
            else: 
                print("\nLa matriz no cumple la regla de linealidad, no pudo ser reparada por lo que no tiene solución por jacobic")    
        else:
            print("\nLa matriz no cumple la regla de linealidad, y dados sus valores no tiene solución por jacobic")

#Main
print("\n\tMetodo de Jacobic\n")
tabla = sol_tabla_33()
print("\nTabla de datos")
print(tabla)
main()