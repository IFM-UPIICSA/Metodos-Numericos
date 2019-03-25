################################     
        #Var asignation
    # Value matrix
row0=[4,-1,1,3]
row1=[2,1,5,3]
row2=[-1,4,1,-2]
matrix=[row0,row1,row2]

    #Diferent Values
VLI = False  # VALIDATE LINEAL INDEPENDENCE
VLI_items = [False,False,False]

#################################
        # Functions

    # Print matrix
def Printmatrix():
    print ("\tOrigninal Matrix")
    for i in range(3):
        for j in range(4):
            if j!=3: print(str(matrix[i][j]),"\t", end="")
            else: print("=\t",str(matrix[i][j]))        
    print("",end="\n")
    
    #Error message by item, number, descripcions
def MensajesError(ele,num,error):
    print(ele,num,error)

    # Linealmente independiente
def VerifyLinealIndep():    
        #Validate zero Column
    if ( (abs(matrix[0][0])) < (( abs(matrix[0][1]) + abs(matrix[0][2]) )) ):
        MensajesError("La fila ",0," no cumple la regla de linealidad")
        VLI_items[0] = False
    else: VLI_items[0] = True

        #Validate first Column
    if ( (abs(matrix[1][1])) < (( abs(matrix[1][0]) + abs(matrix[1][2]) )) ):
        MensajesError("La fila ",1," no cumple la regla de linealidad")
        VLI_items[1] = False
    else: VLI_items[1] = True
        
        #Validate second Column
    if ( (abs(matrix[2][2])) < (( abs(matrix[2][0]) + abs(matrix[2][1]) )) ):
        MensajesError("La fila ",2," no cumple la regla de linealidad")
        VLI_items[2] = False
    else: VLI_items[2] = True

        #Validate All rows
    if ( (VLI_items[0]==True) and (VLI_items[1]==True) and (VLI_items[2]==True) ): VLI = True

    #Try to fix order of matrix
def RepairIndependence():
    print("Some goint to happend here")


################################
        #main
    # funtions calls
Printmatrix()
while (VLI==False):
    VerifyLinealIndep()
    if VLI==False:
        RepairIndependence()