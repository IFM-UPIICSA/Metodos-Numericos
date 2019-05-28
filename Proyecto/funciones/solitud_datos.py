import numpy as np

def sol_No_Datos():
    return (int(input("Ingresa el número de datos: ")))

def sol_Value_Calcular():
    print()
    y = (input("Ingrese el valor a calcular: "))
    return y

# tabla(2,n)
def sol_tabla_2n(n_Datos):
    tabla = np.zeros((2,n_Datos))
    for i in range(0,n_Datos):
        tabla[0][i] = input(f"Ingrese el valor de X{i}: ")
        tabla[1][i] = input(f"Ingrese el valor de Y{i}: ")
    return tabla

# tabla(3,3)
def sol_tabla_33():
    table = np.zeros((3,3))
    for i in range(0,3):
        print()
        table[i][0] = input(f"Ingrese el valor de X{i}: ")
        table[i][1] = input(f"Ingrese el valor de Y{i}: ")
        table[i][2] = input(f"Ingrese el valor de Z{i}: ")
    return table

def sol_array_3():
    b = np.zeros((3))
    print()
    for j in range(0,3):
        b[j] = input(f"Ingrese el valor de b{j}: ")
    return b

def function_grade_n(grade):
    funtion_object = np.zeros((grade))
    for i in range(grade-1,-1,-1):
        if(i!=0):
            print("Ingrese el valor para X^",i)
        else:
            print("Ingrese el valor para el termino independiente")
        funtion_object[i] = int(input()) 
    return funtion_object

def enters(num):
    print("\n"*num)