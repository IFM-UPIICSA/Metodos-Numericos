import numpy
def gaussJordan(matriz, vector):

    matrix = numpy.array(matriz, dtype=numpy.float64)
    vector = numpy.array(vector, dtype=numpy.float64)

    m = len(vector)
    x = numpy.zeros(m)

    for k in range(0, m):
        for r in range(k+1, m):
            factor=(matrix[r,k]/matrix[k,k])
            vector[r]=vector[r]-(factor*vector[k])
            for c in range(0,m):
                matrix[r,c]=matrix[r,c]-(factor*matrix[k,c])

    x[m-1]=vector[m-1]/matrix[m-1, m-1]

    for r in range(m-2, -1, -1):
        suma = 0
        for c in range(0,m):
            suma=suma+matrix[r,c]*x[c]
        x[r]=(vector[r]-suma)/matrix[r, r]  
    return x

#print(gaussJordan([[2,6,1],[1,2,-1],[5,7,-4]],[7,-1,9]))
#print(gaussJordan([[ 1, -3, 1] , [1, 2, 3], [ -1, 9, 7]], [2,5,12]))
print(gaussJordan([[ 2.56, 1.6, 1] , [3.24, 1.8, 1], [ 1.96, 1.4, 1]], [1.6487,2.7182,1]))