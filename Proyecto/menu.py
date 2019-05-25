        #Imports
    #Raices de ecuaciones    
from bisecciones import Bisecciones
from aprox_suces import AproxSuces
from newton_raphson import NewtonRaphson
        #Metodos
def presentacion():
        #Presentacion
    print("\n\n" + ("*"*40))
    print("*" + (" "*38 + "*"))
    print("*" + (" "*13) + "SerMath MN" + (" "*15) + "*")
    print("*" + (" "*38) + "*")
    print("*" + (" "*17) + "By Promidea" + (" "*10) + "*")
    print(("*"*40) + ("\n\n"))
    
def menu_general(): #Opciones de Menu General
    return int(input("Seleccione el tema:\n\n\t1. Raices de Ecuaciones por metodos numericos\n\t2. Sistemas Lineales de Ecuaciones\n\t3. Interpolacion\n\t4. Integracion Numerica\n\t5. Ecuaciones Diferenciales\n\t6. Salir\nR: "))

def menu_1(): #Raices de ecuaciones
        #Seleccionar alguno
    tema = int(input("\nRaices de Ecuaciones por metodos numericos:\n\t1. Bisecciones\n\t2. Aproximaciones Sucesivas\n\t3. Newton Raphson\nR: "))
        #Buscarlo
    if(tema==1): Bisecciones()
    elif(tema==2): AproxSuces()
    elif(tema==3): NewtonRaphson
    else: print("Ingrese un valor valido")

def menu_2(): #Sistemas Lineales de Ecuaciones
        #Seleccionar alguno
    tema = int(input("\nSistemas Lineales de Ecuaciones:\n\t1. Jacobic\n\t2. Gauss Jordan\nR: "))
        #Buscarlo
    if(tema==1): print("Entro a Jacobic")
    elif(tema==2): print("Entro a Gauss Jordan")
    else: print("Ingrese un valor valido")

def main():
    while True: #iterar
        presentacion() #mostrar presentacion
        resul = menu_general() #obtener opcion
            #Buscarla
        if(resul == 1 ):
            menu_1()
        elif(resul==2):
            break
        elif(resul==3):
            break
        elif(resul==4):
            break
        elif(resul==5):
            break
        elif(resul==6):
            break    
        else:
            print("Ingrese un valor valido")
main()