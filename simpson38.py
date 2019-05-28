import numpy as np


def Simpson38(n, x, fx, t):
    sum = 0

    I = h*3/8 * (fx[0]+fx[n]+3*fx[1] + 3*fx[2])
    return I


num = int(input("numero de datos "))
h = float(input("Introduzca h: "))
n = num
x = np.zeros([n])
fx = np.zeros([n])
print("intruduce los datos ")
for i in range(0, n):
    x[i] = input("x[" + str(i) + "]=")
    fx[i] = input("fx[" + str(i) + "]=")
n = num - 1
t = (x[n] - x[0]) / 2
print("el valor de la integral: ", Simpson38(n, x, fx, t))