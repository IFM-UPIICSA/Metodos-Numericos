#############################
#                           #
#          Simpson          #
#              3/8          #
#                           #
#############################
    #Imports
import numpy as np
def Simpson_3_8_Simple():
       #Titulo
    print("\n"*3)
    print("*"*33)
    print("*"+(" "*31)+"*")
    print("*"+(" "*8) + "Simpson 3/8 Simple" + (" "*5)+"*")
    print("*"+(" "*31)+"*")
    print("*"*33)
        #Solicitud de datos
    num = int(input("\nIntroduzca el numero de datos: ")) 
    h = float(input("Introduzca el valor de h: ")) 
    n = num 
    x = np.zeros([n]) 
    fx = np.zeros([n]) 
    print("\nIntruduzca los datos: ") 
    for i in range(0, n): 
        x[i] = input("x[" + str(i) + "]=") 
        fx[i] = input("fx[" + str(i) + "]=") 
    n = num - 1 
    t = (x[n] - x[0]) / 2 
    I = h*3/8 * (fx[0]+fx[n]+3*fx[1] + 3*fx[2]) 
    print("\n\nEl resultado de la integral por Simpson 3/8 Simple es: ", I) 