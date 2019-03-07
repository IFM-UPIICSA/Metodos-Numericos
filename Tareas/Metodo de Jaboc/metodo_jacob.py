        #Var asignation
    # Value matriz
row1=[4,-1,1,3]
row2=[2,1,5,3]
row3=[-1,4,1,-2]
matriz=[row1,row1,row3]

        # Functions

    # Print Matriz
def PrintMatriz():
    print ("\tMatriz Orinal")
    for i in range(3):
        for j in range(4):
            if j!=3:
                print(str(matriz[i][j]),"\t", end="")
            else:
                print("=\t",str(matriz[i][j]))        
    print("",end="\n")

def MensajesError(ele,num,error):
    print(ele,num,error)

    # Linealmente independiente
def VerifyLinealIndep():    
    if ( (abs(matriz[0][0])) < (( abs(matriz[0][1]) + abs(matriz[0][2]) )) ):
        MensajesError("La fila ",0," no cumple la regla de linealidad")
    if ( (abs(matriz[1][1])) < (( abs(matriz[1][0]) + abs(matriz[1][2]) )) ):
        MensajesError("La fila ",1," no cumple la regla de linealidad")
    if ( (abs(matriz[2][2])) < (( abs(matriz[2][0]) + abs(matriz[2][1]) )) ):
        MensajesError("La fila ",2," no cumple la regla de linealidad")
    
    

        #main
    # funtions calls
PrintMatriz()
VerifyLinealIndep()
