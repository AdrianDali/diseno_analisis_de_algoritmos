import matplotlib.pyplot as plt
import numpy  as np
from printer import Printer
#video con el algoritmo https://www.youtube.com/watch?v=tFV4fgxcwOc
###
# Paso 0: contruccion del triangulo original
# Paso 1: Se construye otro triangulo uniendo los puntos medios del triangulo original
# Paso 2: En cada sub triangulo se hace lo mismo
# ###

#Nivele
# s para la recursividad
nivel=10
X,Y=[0],[0]

Raio=1
fator_escala=0.5

printArr = Printer()


for i in range(nivel):
    Xaux,Yaux=[],[]
    Raio=fator_escala*Raio
    #print(f'Raio: {Raio}')
    for k in range(len(X)):
        #print(f'X: {X}')
        for j in range(3):

            #print(f'J: {j} X[k]: {X[k]} y[k]: {Y[k]}')
            Xaux.append(X[k]+Raio*3*np.cos(np.pi/2+j*2*np.pi/3))#
            Yaux.append(Y[k]+Raio*np.sin(np.pi/2+j*2*np.pi/3))
        #print(f'daY:  {Yaux}')
    #a copy of the whole array 
    
    X=Xaux[:]
    Y=Yaux[:]
#print(f'X: {X}')

plt.plot(X,Y,'.')
plt.grid()
plt.axis('equal')
plt.show()