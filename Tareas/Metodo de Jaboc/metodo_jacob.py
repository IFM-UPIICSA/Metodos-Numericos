        #Var asignation
    # Value matriz
row1=[4,-1,1,3]
row2=[2,1,5,3]
row3=[-1,4,1,-2]
matriz=[row1,row1,row3]

        # Functions

    # Print Matriz
def PrintMatriz():
    for i in range(3):
        for j in range(4):
            if j!=3:
                print(str(matriz[i][j]),"\t", end="")
            else:
                print(str(matriz[i][j]))        
    print("",end="\n")

    # Linealmente independiente
def VerifyLinealIndep():
    print("It´s works")



        #main
    # funtions calls
PrintMatriz()
VerifyLinealIndep()
