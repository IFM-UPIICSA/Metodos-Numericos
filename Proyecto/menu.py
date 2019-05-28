        #Imports
    #Raices de ecuaciones    
from bisecciones import Bisecciones
from aprox_suces import AproxSuces
from newton_raphson import NewtonRaphson
    #Sistemas Lineales de Ecuaciones
#from jacobic import Jacobic
from funciones.gauss_method import gaussJordan
    #Interpolacion
from inter_simple_n import InterSimple
from poli_newton import PoliNewton
from lagrange import Lagrange
from method_estadistico import MethodEstadistico
from splines_cubicos import SplinesCubicos
    #Integracion Numerica
from trapecio_simple import Trapecio_Simple
from simpson_1_3_simple import Simpson_1_3_simple
from simpson_3_8_simple import Simpson_3_8_Simple
    #Ecuaciones Diferenciales
from euler import Euler
        #Metodos
def presentacion():
    print("\n\n" + ("*"*40))
    print("*" + (" "*38 + "*"))
    print("*" + (" "*13) + "SerMath MN" + (" "*15) + "*")
    print("*" + (" "*38) + "*")
    print("*" + (" "*17) + "By Promidea" + (" "*10) + "*")
    print(("*"*40) + ("\n\n"))
    
def menu_general(): #Opciones de Menu General
    return int(input("Seleccione el tema:\n\n\t1. Raices de Ecuaciones por metodos numericos\n\t2. Sistemas Lineales de Ecuaciones\n\t3. Interpolacion\n\t4. Integracion Numerica\n\t5. Salir\nR: "))

def menu_1(): #Raices de ecuaciones
    tema = int(input("\nRaices de Ecuaciones por metodos numericos:\n\t1. Bisecciones\n\t2. Aproximaciones Sucesivas\n\t3. Newton Raphson\nR: "))
    if(tema==1): Bisecciones()
    elif(tema==2): AproxSuces()
    elif(tema==3): NewtonRaphson()
    else: print("Ingrese un valor valido")

def menu_2(): #Sistemas Lineales de Ecuaciones
    tema = int(input("\nSistemas Lineales de Ecuaciones:\n\t1. Jacobi\n\t2. Gauss Jordan\nR: "))
    if(tema==1): print("Entro a Jacobi")
    elif(tema==2): print("Entro a Gauss Jordan")
    else: print("Ingrese un valor valido")

def menu_3(): #Interpolacion
    tema = int(input("\nInterpolacion:\n\t1. Simple\n\t2. Polinomio de Newton\n\t3. Lagrange\n\t4. Metodo Estadistico\n\t5. Splines Cubicos\nR: "))
    if(tema==1): InterSimple()
    elif(tema==2): PoliNewton()
    elif(tema==3): Lagrange()
    elif(tema==4): MethodEstadistico()
    elif(tema==5): SplinesCubicos()
    else: print("Ingrese un valor valido")

def menu_4(): #Integracion Numerica
    tema = int(input("\nIntegracion Numerica:\n\t1. Trapecio\n\t2. Simpson 1/3 Simple\n\t3. Simpson 3/8\nR: "))
    if(tema==1): Trapecio_Simple()
    elif(tema==2): Simpson_1_3_simple()
    elif(tema==3): Simpson_3_8_Simple()
    else: print("Ingrese un valor valido")

def main(): #metodo que inicia la ejecucion
    while True: #iteraciones
        presentacion() #mostrar presentacion
        resul = menu_general() #obtener opcion
        if(resul == 1 ):
            menu_1()
        elif(resul==2):
            menu_2()
        elif(resul==3):
            menu_3()
        elif(resul==4):
            menu_4()
        elif(resul==5):
            print("\n\n\tGracias por utilizar SerMath MN\n\n")
            break    
        else:
            print("Ingrese un valor valido")
main()