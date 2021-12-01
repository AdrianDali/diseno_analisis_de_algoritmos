###NUMPY
# potente estructuras de datos 
# implementa matrices y matrices multidimensionales 
# Estas estructuras garantizan calculos eficientes con matrices###
import sys
import numpy as np
import time 
###Numpy Array 
# es un potente objeto de matriz n-dimensional que tiene forma de filas y columnas
# en la que tenemos varios elementos que estan almacenados en sus
# respectivas ubicaciones de memoria###

#NUMPY OCUPA MENOS MEMORIA QUE LA QUE NOS PROPORCIONA EL PROPIO PYTHON
#S= range(1000)
#print('Resultado lista de python: ')
#28000 de memoria con python
#print(sys.getsizeof(5)*len(S))
#print()
##D = np.arange(1000)
#print("resultado numpy array: ")
### 4000 de memoria con np
#print(D.size*D.itemsize)

#Numpy es mas rapido 


SIZE = 10000000

L1 = range(SIZE)
L2 = range(SIZE)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()
result = [(x,y) for x,y in zip(L1,L2)]
print("Resultado en lista pytohn: ")
print((time.time()-start)*1000)
print()
start = time.time()
result = A1+A2
print("Resultado numpy array: ")
print((time.time()-start)*1000)
#Matriz unidimensional
#a = np.array([1,2,3])
#print("1D array: ")
#print(a)
#print()
#Matriz bidimensional
#b= np.array([(1,2,3),(4,5,6)])
#print('2D array: ')
#print(b) 

